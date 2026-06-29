# Huong dan tu dong hoa SEO cho Sago Paint

File nay mo ta quy trinh tu dong hoa cac viec SEO ky thuat co the lam duoc trong repo nay.

## Viec da tu dong hoa

Script chinh:

```bash
node tools/seo-sync.js
```

Script nay tu dong:

- kiem tra chat luong programmatic SEO: URL trung lap, canonical, title/description/H1, trang mong duoi 300 tu, duplicate title/meta description;
- bo qua file xac minh Google dang `google*.html`;
- loai trang `noindex` khoi `sitemap.xml`;

- quet tat ca file `.html` trong project;
- tao lai `sitemap.xml`;
- tao lai `robots.txt`;
- dong bo `canonical` va `og:url` trong tung trang;
- dung domain chinh `https://sagopaint.vn`;
- dung URL khong duoi `.html`, vi Cloudflare Pages dang phuc vu URL dang nay;
- doc file `_redirects` de kiem tra cac redirect cu.

## Lenh thuong dung

Dong bo sitemap, robots va canonical:

```bash
node tools/seo-sync.js
```

Xem truoc thay doi, khong ghi file:

```bash
node tools/seo-sync.js --dry-run
```

Dong bo va deploy len Cloudflare Pages:

```bash
node tools/seo-sync.js --deploy
```

Kiem tra ban live sau khi deploy:

```bash
node tools/seo-sync.js --check-live
```

Dong bo, deploy, roi kiem tra live:

```bash
node tools/seo-sync.js --deploy --check-live
```

Neu doi domain chinh:

```bash
node tools/seo-sync.js --domain=https://ten-domain-moi.vn
```

Neu doi ten Cloudflare Pages project:

```bash
node tools/seo-sync.js --deploy --project=ten-project
```

## Quy trinh khi them trang moi

1. Tao file HTML moi trong repo.
2. Chay:

```bash
node tools/seo-sync.js
```

3. Kiem tra `sitemap.xml` co URL moi.
4. Deploy:

```bash
node tools/seo-sync.js --deploy --check-live
```

5. Vao Google Search Console > So do trang web > gui lai:

```txt
sitemap.xml
```

## Quy trinh khi thay URL

Neu doi URL cu sang URL moi, them redirect vao file `_redirects`.

Vi du:

```txt
/url-cu/ /url-moi 301
```

Sau do chay:

```bash
node tools/seo-sync.js --deploy --check-live
```

## Nhung viec khong the tu dong hoa hoan toan

Google khong cho API de ep lap chi muc hang loat cho website thuong.

Nhung viec van nen lam trong Google Search Console:

- gui lai `sitemap.xml`;
- dung Kiem tra URL cho vai trang quan trong;
- bam Yeu cau lap chi muc cho trang chu va cac trang san pham/danh muc chinh;
- theo doi muc Trang de xem loi 404, redirect, canonical, hoac da thu thap du lieu nhung chua lap chi muc.

Indexing API cua Google chi dung cho `JobPosting` hoac livestream video `BroadcastEvent`, khong phu hop cho cac trang san pham son cua site nay.

## URL uu tien yeu cau lap chi muc

```txt
https://sagopaint.vn/
https://sagopaint.vn/son-noi-that
https://sagopaint.vn/son-ngoai-that
https://sagopaint.vn/son-chong-tham
https://sagopaint.vn/tinh-son/
https://sagopaint.vn/phong-thuy-son-nha/
```

## Ghi chu ve 404 cu

Neu Search Console bao cac URL dang WordPress cu nhu:

```txt
/wp-content/...
/wp-*.php
```

thi co the bo qua neu site hien tai khong con dung WordPress. Google se tu loai dan cac URL do khoi bao cao.
