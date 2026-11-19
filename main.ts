// news-image-20261119 — copy entry.png to the make.fun output directory.
// Node 22 stdlib only. No network. Deterministic: byte-identical copy,
// so both grading runs write the same bytes.
// Override the destination with MAKEFUN_OUTPUT_DIR (default: /output).
import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const src = join(here, "entry.png");
const outDir = resolve(process.env.MAKEFUN_OUTPUT_DIR ?? "/output");
if (!existsSync(src)) {
  console.error(`entry.png not found next to main.ts: ${src}`);
  process.exit(1);
}
mkdirSync(outDir, { recursive: true });
const dest = join(outDir, "entry.png");
copyFileSync(src, dest);
console.log(`copied entry.png -> ${dest}`);
