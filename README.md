# pcg-update-host

# 🧠 PCG Model Update Host

這個 GitHub 倉庫是用來提供 **Phonocardiogram (PCG) 心音模型的遠端更新**功能，搭配 Android 應用程式使用。當 App 使用者點擊「檢查更新」，會從此處下載最新的 `.pt` 模型檔案。

---

## 📦 檔案說明

| 檔案名稱 | 說明 |
|----------|------|
| `update-file.pt` | 最新的 PyTorch 模型檔案。App 將會下載並覆寫本機模型以更新。 |

---

## 🔄 更新流程（App 對接方式）

1. Android App 呼叫 URL：  
   [`https://raw.githubusercontent.com/cno77766612/pcg-update-host/main/update-file.pt`](https://raw.githubusercontent.com/cno77766612/pcg-update-host/main/update-file.pt)
2. 將其儲存至本機（例如 `model_updated.pt`）
3. 下次開啟自動載入更新後的模型

---

## 📌 使用說明

此模型適用於：

- 單通道 PCG 信號分析
- 輸入長度為 6000 的時間序列
- 可用於二分類（正常 vs 異常）

---

## 🗂️ 歷史版本

| 版本 | 日期 | 說明 |
|------|------|------|
| v1.0.0 | 2024-04-21 | 初始上傳版本 |

---

## 🛡️ 安全性與驗證

建議未來搭配 `version.txt` + `checksum` 雜湊驗證模型完整性。

---

## 🧑‍💻 作者

- GitHub: [@cno77766612](https://github.com/cno77766612)
- 專案用途：學術 / 測試 / 教學
