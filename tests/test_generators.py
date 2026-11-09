import importlib.util
import json
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tools" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class GeneratorRegression(unittest.TestCase):
    def assert_shared_stylesheet(self, output, relative_page):
        href = '../' * (len(Path(relative_page).parts) - 1) + 'assets/css/site-base.css'
        self.assertIn(f'href="{href}"', output)
        self.assertEqual((ROOT / relative_page).parent.joinpath(href).resolve(),
                         ROOT / 'assets/css/site-base.css')

    def test_refresh_never_overwrites_non_product_pages_or_index_controls(self):
        refresh = load("refresh_pages")
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            for file in ROOT.glob("*.html"):
                shutil.copyfile(file, target / file.name)
            protected = {p.name: p.read_bytes() for p in target.glob("*.html")
                         if not refresh.is_product_page(p) and p.name not in refresh.CATEGORY_META}
            heads = {p.name: re.search(r"<head.*?</head>", p.read_text(encoding="utf-8"), re.S).group()
                     for p in target.glob("*.html") if refresh.is_product_page(p)}
            self.assertIn("blog.html", protected)
            self.assertIn("google4bd4155c856d151b.html", protected)
            refresh.ROOT = target
            refresh.main()
            for name, content in protected.items():
                self.assertEqual((target / name).read_bytes(), content, name)
            for name, head in heads.items():
                output = (target / name).read_text(encoding="utf-8")
                strip_schema = lambda text: re.sub(r'<script\b[^>]*type="application/ld\+json"[^>]*>.*?</script>', '', text, flags=re.S)
                output_head = re.search(r"<head.*?</head>", output, re.S).group()
                self.assertEqual(strip_schema(head), strip_schema(output_head), name)
                self.assert_shared_stylesheet(output, name)
                self.assertIn('href="#main-content"', output)
                for image in re.findall(r'<img\b[^>]+>', output):
                    self.assertIn('width="', image)
                    self.assertIn('height="', image)
            alias = (target / "son-noi-that-lau-chui-hieu-qua-anaclean-be-mat-ban-bong-2.html").read_text(encoding="utf-8")
            self.assertIn('content="noindex, follow"', alias)
            self.assertIn('href="https://sagopaint.vn/son-noi-that-lau-chui-hieu-qua-anaclean-be-mat-ban-bong"', alias)

    def test_dry_faq_uses_duration_and_refresh_syncs_only_generated_schema(self):
        refresh = load("refresh_pages")
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            for file in ROOT.glob("*.html"):
                shutil.copyfile(file, target / file.name)
            refresh.ROOT = target
            refresh.main()
            powder = (target / "bot-tret-noi-that-hoasen-ana.html").read_text(encoding="utf-8")
            satin = (target / "son-ngoai-that-ana-satin-be-mat-ban-bong.html").read_text(encoding="utf-8")
            self.assertIn('Thời gian khô: 16 giờ', powder)
            self.assertNotIn('class="accordion-body">Khối lượng thể tích', powder)
            self.assertIn('Khô bề mặt: 30 phút; Sơn lớp kế tiếp: 120 phút', satin)
            def schemas(text):
                return [json.loads(x) for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S)]
            self.assertIn('Khô bề mặt: 30 phút; Sơn lớp kế tiếp: 120 phút', json.dumps(schemas(satin), ensure_ascii=False))
            original = (ROOT / "son-ngoai-that-ana-satin-be-mat-ban-bong.html").read_text(encoding="utf-8")
            def without_generated(value):
                if isinstance(value, list): return [without_generated(x) for x in value if not isinstance(x, dict) or x.get('@type') != 'FAQPage']
                if isinstance(value, dict): return {k: without_generated(v) for k, v in value.items()}
                return value
            self.assertEqual(without_generated(schemas(original)), without_generated(schemas(satin)))
            category = (target / 'son-noi-that.html').read_text(encoding='utf-8')
            self.assertNotIn('son-noi-that-lau-chui-hieu-qua-anaclean-be-mat-ban-bong-2', category)
            self.assertNotIn('son-noi-that-lau-chui-hieu-qua-anaclean-be-mat-ban-bong-2', powder)
            local = refresh.extract_product(target / 'sago-s-68-pro-chong-tham-a-nang-lo-thien-cao-cap.html')
            self.assertEqual(local['image'], 'assets/products/sago-s68-pro-preview.webp')
            self.assertEqual(local['name'], 'SAGO S 68 PRO - CHỐNG THẤM ĐA NĂNG LỘ THIÊN CAO CẤP')
            self.assertEqual(refresh.display_name(local), 'SAGO S 68 PRO chống thấm đa năng lộ thiên cao cấp')
            self.assertIn('>SAGO S 68 PRO chống thấm đa năng lộ thiên cao cấp</h1>', refresh.render_product(local, []))
            new = refresh.render_product(refresh.extract_product(target / 'bot-tret-noi-that-hoasen-ana.html'), [])
            self.assertNotIn('https://sagopaint.vn/https://', new)
            self.assertIn('https://cdn.sagopaint.vn/assets/products/bot-tret-noi-that-hoasen-ana.png', new)

    def test_curated_product_description_survives_refresh_without_truncation(self):
        refresh = load("refresh_pages")
        description = ('Sơn thử có bề mặt dễ lau chùi & phù hợp cho phòng khách. '
                       'Nội dung biên tập giữ trọn câu với dấu "ngoặc kép", thay vì bị cắt giữa ý khi dài hơn giới hạn cũ. '
                       'Khách hàng có thể đọc đủ thông tin trước khi chọn sơn.')
        self.assertGreater(len(description), 155)
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / 'son-thu.html'
            file.write_text('<head><meta content="' + refresh.esc(description)
                            + '" name="description"></head>'
                            + '<script type="application/ld+json">{"@type":"Product","name":"Sơn thử"}</script>'
                            + '<h1 class="product-hero-title">Sơn thử</h1>'
                            + '<p class="detail-copy">Chi tiết khác không được thay mô tả biên tập.</p>', encoding='utf-8')
            product = refresh.extract_product(file)
            self.assertEqual(product['description'], description)
            output = refresh.render_product(product, [])
            self.assertIn('<meta name="description" content="' + refresh.esc(description) + '">', output)
            self.assertIn('<p class="product-hero-copy">' + refresh.esc(description) + '</p>', output)
            schemas = [json.loads(block) for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', output, re.S)]
            self.assertEqual(next(item for schema in schemas for item in schema if item.get('@type') == 'Product')['description'], description)
            file.write_text(output, encoding='utf-8')
            self.assertEqual(refresh.extract_product(file)['description'], description)

    def test_product_recognition_requires_valid_product_schema(self):
        refresh = load("refresh_pages")
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "article.html"
            for data, expected in [("not json", False), ('{"@type":"Article"}', False),
                                   ('{"@graph":[{"@type":["Thing","Product"]}]}', True)]:
                file.write_text(f'<script type="application/ld+json">{data}</script>', encoding="utf-8")
                self.assertEqual(refresh.is_product_page(file), expected)

    def test_new_product_head_uses_clean_canonical_and_shared_font(self):
        refresh = load("refresh_pages")
        output = refresh.head("Sơn thử", "Mô tả sản phẩm", "son-thu.html")
        self.assertIn('href="https://sagopaint.vn/son-thu"', output)
        self.assertIn('family=Be+Vietnam+Pro', output)
        self.assert_shared_stylesheet(output, 'son-thu.html')

    def test_invalid_existing_head_stops_refresh_before_any_write(self):
        refresh = load("refresh_pages")
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            for file in ROOT.glob("*.html"):
                shutil.copyfile(file, target / file.name)
            product = sorted(p for p in target.glob("*.html") if refresh.is_product_page(p))[-1]
            product.write_text(product.read_text(encoding="utf-8").replace("<head>", ""), encoding="utf-8")
            before = {p: p.read_bytes() for p in target.glob("*.html")}
            refresh.ROOT = target
            with self.assertRaisesRegex(ValueError, 'refusing to overwrite metadata'):
                refresh.main()
            for path, content in before.items():
                self.assertEqual(path.read_bytes(), content)

    def test_fengshui_generation_at_both_depths_has_absolute_images_and_shared_ui(self):
        feng = load("generate_fengshui_pages")
        with tempfile.TemporaryDirectory() as directory:
            feng.OUT = Path(directory)
            feng.main()
            files = list(feng.OUT.rglob("*.html"))
            self.assertEqual(len(files), 17)
            for file in files:
                output = file.read_text(encoding="utf-8")
                self.assertNotIn('../https://', output)
                self.assertNotIn('https://sagopaint.vn/https://', output)
                self.assertIn('property="og:image" content="https://cdn.sagopaint.vn/assets/sago-logo.png"', output)
                self.assertIn('name="twitter:image" content="https://cdn.sagopaint.vn/assets/sago-logo.png"', output)
                schemas = [json.loads(block) for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', output, re.S)]
                article = next(item for schema in schemas for item in (schema if isinstance(schema, list) else [schema]) if item.get('@type') == 'Article')
                self.assertEqual(article['publisher']['logo']['url'], 'https://cdn.sagopaint.vn/assets/sago-logo.png')
                self.assertNotRegex(output, r'<img[^>]+src="/assets/')
                for src in re.findall(r'<img[^>]+src="([^"]+)"', output):
                    if src.endswith('assets/products/sago-s68-pro-preview.webp'):
                        depth = len(file.relative_to(feng.OUT).parts)
                        self.assertEqual(src, '../' * depth + 'assets/products/sago-s68-pro-preview.webp')
                        self.assertTrue((ROOT / 'phong-thuy-son-nha' / file.relative_to(feng.OUT)).parent.joinpath(src).is_file())
                self.assertIn('family=Be+Vietnam+Pro', output)
                self.assert_shared_stylesheet(output, Path('phong-thuy-son-nha') / file.relative_to(feng.OUT))
                self.assertIn('id="main-content"', output)
                self.assertIn('href="#main-content"', output)

    def test_blog_generation_preserves_font_and_links_to_orphan_guides(self):
        blog = load("generate_blog_pages")
        with tempfile.TemporaryDirectory() as directory:
            blog.ROOT = Path(directory)
            (blog.ROOT / 'sitemap.xml').write_text('<urlset></urlset>', encoding='utf-8')
            blog.main()
            self.assertEqual(len(list(blog.ROOT.glob('*.html'))), 6)
            for file in blog.ROOT.glob('*.html'):
                output = file.read_text(encoding='utf-8')
                self.assertIn('family=Be+Vietnam+Pro', output)
                self.assert_shared_stylesheet(output, file.name)
                self.assertIn('id="main-content"', output)
            output = (blog.ROOT / 'blog.html').read_text(encoding='utf-8')
            self.assertIn('/cach-tinh-luong-son-can-dung', output)
            self.assertIn('/mau-son-phong-khach-nha-nho', output)
            self.assertIn('/son-nha-hop-phong-thuy-2026', output)


if __name__ == '__main__':
    unittest.main()
