# Revenue Architecture Web App

Flask製の Revenue Architecture Dashboard です。CVR / CAC / LTV / ROAS / ROI を入力値から自動計算し、Revenue Funnel と Before / After を1画面で可視化します。

## 構成

- `app.py` Flask本体
- `templates/index.html` テンプレート
- `static/style.css` スタイル
- `requirements.txt` 依存関係
- `render.yaml` Renderデプロイ設定

## ローカル起動

```bash
python -m venv .venv
source .venv/bin/activate  # Windowsは .venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

ブラウザで `http://127.0.0.1:5000` を開きます。

## GitHubにアップロード

```bash
git init
git add .
git commit -m "Initial commit: Revenue Architecture Web App"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

## Renderで公開

1. Render にログイン
2. `New +` → `Blueprint` もしくは `Web Service`
3. GitHubリポジトリを接続
4. `render.yaml` を使う場合は自動で設定反映
5. デプロイ完了後、公開URLで確認

## 指標ロジック

- Revenue = `Customer * 単価`
- CVR = `Customer / Traffic`
- CAC = `広告費 / Customer`
- LTV/CAC = `LTV / CAC`
- ROAS = `Revenue / 広告費`
- ROI = `(Revenue - 広告費) / 広告費`

## 次の拡張候補

- CSVアップロード
- 月別推移グラフ
- Google Sheets連携
- ログイン機能
- 面接用ポートフォリオ説明文の同梱


## Japanese PDF font

The uploaded font is included at `static/fonts/NotoSansJP-VariableFont_wght.ttf` for Japanese PDF generation.
