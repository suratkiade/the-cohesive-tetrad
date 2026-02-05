# Audit Forensik Mikroskopik: GitHub Wiki & Repo 

## Ringkasan akses sumber eksternal
Audit wiki GitHub https://github.com/suratkiade/risalah-saloqum/wiki gagal dilakukan secara langsung karena koneksi ke GitHub diblokir dari lingkungan ini. Bukti perintah dan respons dicatat di bawah.

```text
$ git clone --depth 1 https://github.com/suratkiade/risalah-saloqum.wiki.git /workspace/risalah-saloqum.wiki
Cloning into '/workspace/risalah-saloqum.wiki'...
fatal: unable to access 'https://github.com/suratkiade/risalah-saloqum.wiki.git/': CONNECT tunnel failed, response 403
```

```text
$ curl -I https://github.com/suratkiade/risalah-saloqum/wiki
curl: (56) CONNECT tunnel failed, response 403
HTTP/1.1 403 Forbidden
content-length: 9
content-type: text/plain
date: Thu, 05 Feb 2026 03:05:04 GMT
server: envoy
connection: close
```

## Ruang lingkup audit lokal
Karena wiki eksternal tidak dapat diakses, audit forensik difokuskan pada artefak dan skrip di repo lokal ini sebagai proksi ketaatan standar wiki (struktur, navigasi, metadata, audit trail, dan pemeliharaan dokumen).

## Observasi awal tentang standar wiki (ringkas)
Standar wiki yang dinilai dalam audit ini meliputi: 
1. **Halaman indeks/landing yang jelas** (tujuan, ringkasan, metadata, dan rujukan utama).
2. **Navigasi/tautan silang** antar halaman inti.
3. **Konsistensi format** (judul, struktur, terminologi) dan metadata.
4. **Jejak audit & perubahan** (changelog, audit report, checksum).
5. **Kepatuhan sitasi & lisensi**.
6. **Keandalan skrip pemeliharaan** (validasi skema, checksum, link).

