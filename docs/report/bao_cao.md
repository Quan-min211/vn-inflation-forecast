# BÁO CÁO GIẢI THÍCH PHƯƠNG PHÁP PHÂN TÍCH

**Đề tài:** Phân tích các yếu tố vĩ mô tác động đến lạm phát tại Việt Nam giai đoạn 1996–2022

---

## 1. Lý thuyết "Bệnh tự miễn" trong Lạm phát

### 1.1 Khái niệm

Trong y học, bệnh tự miễn là khi hệ miễn dịch của cơ thể tấn công chính các tế bào khỏe mạnh của mình — tức là cơ thể tự gây bệnh cho chính mình mà không cần tác nhân bên ngoài.

Nhóm mượn hình ảnh này để mô tả một hiện tượng kinh tế: **Lạm phát tự duy trì chính nó mà không cần cú sốc từ bên ngoài.** Cơ chế hoạt động như sau:

1. Năm ngoái giá cả tăng 10%.
2. Người dân và doanh nghiệp **kỳ vọng** rằng năm nay giá cả sẽ tiếp tục tăng.
3. Doanh nghiệp **chủ động tăng giá bán** để bù đắp chi phí dự kiến.
4. Người lao động **đòi tăng lương** vì sợ mất sức mua.
5. Chi phí sản xuất tăng do lương tăng → giá cả tiếp tục tăng → quay lại bước 1.

Đây là một **vòng lặp tự củng cố**: lạm phát quá khứ tạo ra kỳ vọng, kỳ vọng tạo ra hành vi, hành vi tạo ra lạm phát thực tế cho kỳ tiếp theo. Không cần GDP tăng nóng, không cần tỷ giá biến động, không cần lãi suất thay đổi — lạm phát vẫn tự kéo dài.

### 1.2 Đối lập: "Tác nhân bên ngoài"

Ngược lại với Bệnh tự miễn, giả thuyết Tác nhân bên ngoài cho rằng lạm phát Việt Nam chủ yếu bị chi phối bởi các yếu tố kinh tế vĩ mô:

- **GDP tăng nóng** → cầu vượt cung → giá tăng (kênh Cầu kéo).
- **Tỷ giá VND mất giá** → hàng nhập khẩu đắt hơn → chi phí sản xuất tăng → giá tăng (kênh Chi phí đẩy).
- **Lãi suất giảm** → doanh nghiệp vay nhiều hơn → tiền trong nền kinh tế tăng → giá tăng (kênh Tiền tệ).

### 1.3 Câu hỏi của đồ án

> Trong 3 thập kỷ qua, lạm phát Việt Nam chủ yếu là do "Bệnh tự miễn" hay do "Tác nhân bên ngoài"?

Để trả lời, nhóm sử dụng công cụ **FEVD — Phân rã Phương sai** từ mô hình VAR. Nếu CPI tự giải thích phần lớn biến động của chính nó qua nhiều kỳ, kết luận nghiêng về Bệnh tự miễn.

---

## 2. Pipeline Phân tích — Tổng quan Đường đi của Dữ liệu

Toàn bộ quá trình phân tích được thiết kế tối giản theo chuỗi 6 bước, mỗi bước phục vụ trực tiếp cho câu hỏi nghiên cứu:

```
📂 Dữ liệu Thô (Excel · 27 năm · 11 biến)
        ↓
🧹 Làm sạch (Nội suy missing · Giữ 4 biến)
        ↓
📊 Kiểm định bắt buộc (ADF Test · Sai phân · VIF)
        ↓
🤖 Mô hình VAR(1) (Ước lượng 4 phương trình đồng thời)
        ↓
🔬 FEVD 10 kỳ (Phân rã phương sai — Bằng chứng chính)
  + Granger Causality, IRF (Kiểm tra phụ)
        ↓
✅ Kết luận: CPI tự giải thích phần lớn → QUÁN TÍNH
```

Mỗi bước trong pipeline có một nhiệm vụ duy nhất và là tiền đề bắt buộc cho bước tiếp theo. Bỏ bất kỳ bước nào sẽ làm mất tính hợp lệ của kết luận cuối cùng.

---

## 3. Biểu đồ Chuỗi CPI Growth trên Trang Home

### 3.1 Tác dụng

Biểu đồ chuỗi CPI growth rate từ 1996 đến 2022 trên trang Home không phải để phân tích chuyên sâu — nó là biểu đồ **định vị câu hỏi** cho người xem dashboard. Khi nhìn vào biểu đồ này, người xem ngay lập tức thấy được:

- Lạm phát Việt Nam có hai đỉnh bất thường lớn vào năm 2008 và 2011.
- Sau 2012, lạm phát hạ nhiệt và ổn định dưới 5%.
- Đường trung bình (đường nét đứt đỏ) cho thấy mức lạm phát trung bình lịch sử.

### 3.2 Dữ liệu để vẽ

Biểu đồ được vẽ trực tiếp từ cột `cpi_growth_percent` trong dataset đã làm sạch. Trục X là năm, trục Y là tỷ lệ tăng CPI hàng năm (%). Đường nét đứt đỏ là giá trị trung bình (mean) của toàn bộ chuỗi.

### 3.3 Kết luận nên rút ra

Nhìn vào biểu đồ, ta thấy CPI growth có xu hướng **tự quay về mức trung bình** sau mỗi đợt tăng đột biến — đây là dấu hiệu trực quan đầu tiên gợi ý tính quán tính: lạm phát tự kéo dài một thời gian rồi tự hạ nhiệt, chứ không phải giảm ngay khi cú sốc bên ngoài biến mất. Tuy nhiên, đây chỉ là quan sát bằng mắt — cần FEVD để chứng minh bằng số liệu.

> 📷 **Chụp biểu đồ này từ trang Home** của Streamlit để chèn vào báo cáo.

---

## 4. Tổng quan Dữ liệu

### 4.1 Dữ liệu ban đầu

Dataset gốc `dataset_project1.xlsx` từ World Bank chứa:

- **27 dòng** — mỗi dòng là một năm, từ 1996 đến 2022.
- **11 biến kinh tế** — đại diện cho 4 trụ cột vĩ mô: Giá cả, Tăng trưởng, Tiền tệ, và Đối ngoại.

### 4.2 Tại sao chỉ giữ 4 biến?

Mô hình VAR ước lượng **đồng thời nhiều phương trình hồi quy** — mỗi biến là một phương trình riêng. Với mỗi biến thêm vào, số lượng tham số (hệ số) cần ước lượng tăng lên rất nhanh.

Quy tắc kinh nghiệm thống kê: **số quan sát phải lớn hơn nhiều lần số tham số.** Với 27 năm dữ liệu:
- VAR(1) với 4 biến cần ước lượng khoảng 20 tham số → hợp lệ.
- VAR(1) với 11 biến cần ước lượng khoảng 132 tham số → **nhiều hơn cả số quan sát**, dẫn đến quá khớp (overfitting) nghiêm trọng và kết quả hoàn toàn không đáng tin.

Vì vậy, nhóm chọn **1 biến đại diện mạnh nhất** cho mỗi kênh truyền dẫn lạm phát, đảm bảo mỗi kênh được phản ánh mà không gây quá khớp.

### 4.3 Bốn biến được chọn — Chi tiết từng biến

#### Biến 1: `cpi_growth_percent` — Biến mục tiêu

- **Ý nghĩa:** Tốc độ tăng chỉ số giá tiêu dùng hàng năm, tính bằng %. Đây là thước đo lạm phát phổ biến nhất — nó cho biết giỏ hàng hóa mà hộ gia đình mua hàng ngày (thực phẩm, xăng, điện, nhà ở...) đắt lên bao nhiêu phần trăm so với năm trước.
- **Vai trò trong VAR:** Biến mục tiêu. Toàn bộ phân tích xoay quanh việc tìm hiểu biến động của biến này.
- **Trong FEVD:** Là biến được "phân rã" — ta đo xem sai số dự báo của biến này đến từ chính nó bao nhiêu %, từ các biến khác bao nhiêu %.

#### Biến 2: `gdp_growth_percent` — Tác nhân bên ngoài: Cầu kéo

- **Ý nghĩa:** Tốc độ tăng trưởng GDP thực hàng năm, tính bằng %. Đo lường sức khỏe tổng thể của nền kinh tế — nền kinh tế đang mở rộng hay thu hẹp.
- **Vai trò trong VAR:** Đại diện cho kênh **Cầu kéo** (Demand-pull). Khi GDP tăng nóng, tổng cầu vượt tổng cung, doanh nghiệp có cớ tăng giá, dẫn đến lạm phát. Nếu GDP có đóng góp lớn trong FEVD, nghĩa là lạm phát VN bị kéo bởi tăng trưởng kinh tế chứ không phải tự phát.

#### Biến 3: `lending_interest_percent` — Tác nhân bên ngoài: Kênh Tiền tệ

- **Ý nghĩa:** Lãi suất cho vay bình quân hàng năm, tính bằng %. Đây là giá cả của việc vay tiền — lãi suất cao nghĩa là tiền đắt, lãi suất thấp nghĩa là tiền rẻ.
- **Vai trò trong VAR:** Đại diện cho kênh **Tiền tệ** (Monetary channel). Khi Ngân hàng Nhà nước hạ lãi suất, doanh nghiệp và người dân vay nhiều hơn, lượng tiền trong nền kinh tế tăng, dẫn đến giá cả tăng. Nếu lãi suất có đóng góp lớn trong FEVD, nghĩa là chính sách tiền tệ là nguyên nhân chính của lạm phát.

#### Biến 4: `officical_exchange_rate_percent` — Tác nhân bên ngoài: Chi phí đẩy

- **Ý nghĩa:** Tỷ giá hối đoái chính thức VND/USD. Đo lường giá trị đồng Việt Nam so với đồng USD.
- **Vai trò trong VAR:** Đại diện cho kênh **Chi phí đẩy** (Cost-push) từ bên ngoài. Khi VND mất giá so với USD, hàng nhập khẩu (xăng dầu, nguyên liệu, linh kiện) trở nên đắt hơn, chi phí sản xuất tăng, buộc doanh nghiệp tăng giá bán, dẫn đến lạm phát. Nếu tỷ giá có đóng góp lớn trong FEVD, nghĩa là lạm phát VN chủ yếu bị "nhập khẩu" từ bên ngoài.

---

## 5. Kiểm định Bắt buộc Trước Khi Chạy VAR

### 5.1 Tại sao phải kiểm định?

Mô hình VAR có một yêu cầu toán học nghiêm ngặt: **tất cả các chuỗi đầu vào phải "dừng" (stationary).** Nếu đưa chuỗi không dừng vào VAR, kết quả sẽ bị "tương quan giả" (Spurious Regression) — tức là mô hình cho ra mối quan hệ trông có vẻ rất mạnh giữa hai biến, nhưng thực tế mối quan hệ đó hoàn toàn không tồn tại.

Ví dụ: Nếu đưa "Dân số Việt Nam" và "Số lượng iPhone bán ra toàn cầu" vào cùng một mô hình mà không kiểm tra tính dừng, mô hình sẽ kết luận hai biến này có quan hệ cực mạnh — đơn giản vì cả hai đều tăng liên tục theo thời gian. Nhưng rõ ràng dân số VN không gây ra doanh số iPhone.

Vì vậy, trước khi chạy VAR, ta **bắt buộc** phải:
1. Kiểm tra ADF để xem chuỗi nào dừng, chuỗi nào không.
2. Sai phân các chuỗi không dừng.
3. Kiểm tra VIF để đảm bảo các biến không mang thông tin trùng lặp.

---

### 5.2 ADF Test — Trước xử lý

#### ADF là gì?

ADF — Augmented Dickey-Fuller — là kiểm định thống kê để trả lời câu hỏi: **Chuỗi dữ liệu này có "dừng" hay không?**

**Chuỗi dừng** là chuỗi mà giá trị trung bình và mức dao động (phương sai) không thay đổi theo thời gian. Ví dụ: nhiệt độ ở Sài Gòn dao động quanh 28–34°C quanh năm — đây là chuỗi dừng.

**Chuỗi không dừng** là chuỗi mà giá trị trung bình hoặc mức dao động thay đổi theo thời gian. Ví dụ: giá nhà ở Sài Gòn cứ tăng liên tục qua từng năm — đây là chuỗi không dừng.

#### ADF tính như thế nào?

ADF kiểm tra xem chuỗi có "đơn vị root" (unit root) hay không. Nếu có đơn vị root, chuỗi không dừng. Cụ thể:

- ADF chạy một phương trình hồi quy đặc biệt trên chuỗi dữ liệu.
- Từ phương trình đó, nó tính ra một **ADF statistic** (giá trị thống kê) và một **p-value**.
- **Quy tắc đọc kết quả:**
  - Nếu p-value **nhỏ hơn 0.05** → Bác bỏ giả thuyết "chuỗi không dừng" → Kết luận: **chuỗi DỪNG**.
  - Nếu p-value **lớn hơn hoặc bằng 0.05** → Không bác bỏ được → Kết luận: **chuỗi KHÔNG DỪNG**.

#### Nhìn vào bảng ADF trước xử lý, kết luận gì?

Bảng ADF "Trước xử lý" cho thấy:

- Một số biến có p-value nhỏ hơn 0.05 → dừng sẵn → có thể đưa thẳng vào VAR.
- Một số biến có p-value lớn hơn 0.05 → **không dừng** → cần phải xử lý thêm bằng sai phân trước khi đưa vào VAR.

> 📷 **Chụp bảng ADF "trước xử lý"** từ trang Stationarity Testing trên Streamlit.

---

### 5.3 Sai phân là gì? Vai trò trong bài

#### Định nghĩa

Sai phân bậc 1 (first-order differencing) là phép biến đổi: lấy giá trị năm nay trừ đi giá trị năm trước.

```
Giá trị sai phân = Giá trị năm t − Giá trị năm (t−1)
```

Ví dụ: Tỷ giá VND/USD năm 2020 là 23.200, năm 2019 là 23.050. Sai phân = 23.200 − 23.050 = 150. Con số 150 này cho biết **mức thay đổi** trong năm đó, thay vì giá trị tuyệt đối.

#### Tại sao sai phân giúp chuỗi trở nên "dừng"?

Chuỗi không dừng thường có xu hướng tăng hoặc giảm liên tục. Khi lấy sai phân, ta loại bỏ xu hướng đó và chỉ giữ lại phần **dao động** — phần dao động này thường dừng.

#### Vai trò trong bài

Trong đồ án, các biến không vượt qua ADF Test được lấy sai phân bậc 1. Sau đó, các biến đã sai phân được kiểm định lại bằng ADF để xác nhận đã dừng. Chỉ khi toàn bộ bộ biến đều dừng, ta mới được phép đưa vào mô hình VAR.

Lưu ý: Khi lấy sai phân, ta mất 1 quan sát (vì năm đầu tiên không có năm trước để trừ). Từ 27 quan sát, sau sai phân còn khoảng 25–26 quan sát.

---

### 5.4 ADF Test — Sau xử lý

#### "Sau xử lý" nghĩa là gì?

"Sau xử lý" nghĩa là sau khi đã lấy sai phân cho các biến không dừng. Bảng ADF "sau xử lý" kiểm tra lại toàn bộ 4 biến một lần nữa trên dữ liệu đã sai phân.

#### Tại sao phải chia Trước và Sau?

- **Trước xử lý:** Để biết biến nào dừng sẵn, biến nào cần sai phân. Nếu một biến đã dừng sẵn, không nên sai phân nó — vì sai phân một chuỗi đã dừng sẽ làm mất thông tin vô ích.
- **Sau xử lý:** Để xác nhận rằng sai phân đã thực sự giải quyết vấn đề. Đôi khi sai phân bậc 1 chưa đủ và cần sai phân bậc 2 — bảng "sau xử lý" giúp phát hiện trường hợp này.

#### Kết quả kỳ vọng

Sau xử lý, tất cả 4 biến phải có p-value nhỏ hơn 0.05 — tức là tất cả đều DỪNG. Đây là điều kiện tiên quyết để bước tiếp theo (VAR) có ý nghĩa.

> 📷 **Chụp bảng ADF "sau xử lý"** từ trang Stationarity Testing trên Streamlit.

---

### 5.5 VIF — Kiểm tra Đa cộng tuyến

#### VIF là gì?

VIF — Variance Inflation Factor — là chỉ số đo mức độ **trùng lặp thông tin** giữa các biến. Nếu hai biến mang thông tin gần giống nhau (ví dụ: Import Index và Export Index đều phản ánh hoạt động thương mại), đưa cả hai vào mô hình sẽ khiến mô hình không thể phân biệt được ảnh hưởng riêng của từng biến.

#### Cách đọc kết quả

- **VIF bằng 1:** Biến hoàn toàn độc lập, không trùng thông tin với biến nào khác.
- **VIF từ 1 đến 5:** Mức chấp nhận được.
- **VIF từ 5 đến 10:** Cần lưu ý, có dấu hiệu trùng lặp.
- **VIF lớn hơn 10:** Đa cộng tuyến nghiêm trọng — cần loại biến hoặc biến đổi dữ liệu.

#### Tại sao phải kiểm VIF trước VAR?

Nếu đưa các biến có VIF cao vào VAR, hệ số hồi quy sẽ bị "phồng lên" — tức là hệ số có thể rất lớn hoặc rất nhỏ một cách vô nghĩa, và thay đổi mạnh chỉ vì thêm hoặc bớt một quan sát. Kết quả FEVD sẽ không đáng tin vì nó dựa trên các hệ số VAR.

Với bộ 4 biến đã sai phân, VIF của từng biến cần nằm dưới ngưỡng 10 để đảm bảo các kết luận từ VAR là đáng tin cậy.

> 📷 **Chụp bảng VIF** từ trang Stationarity Testing trên Streamlit.

---

## 6. Mô hình VAR và FEVD

### 6.1 VAR hoạt động như thế nào?

#### Ý tưởng cốt lõi

VAR — Vector Autoregression — là mô hình trong đó **mỗi biến được dự báo dựa trên giá trị quá khứ của tất cả các biến** (bao gồm cả chính nó). Không có biến nào được xem là "nguyên nhân" hay "kết quả" trước — VAR để dữ liệu tự nói.

Với 4 biến trong đồ án, VAR(1) gồm 4 phương trình hồi quy chạy đồng thời:

```
CPI năm nay     = a₁×CPI năm trước   + a₂×GDP năm trước   + a₃×Lãi suất năm trước + a₄×Tỷ giá năm trước + sốc CPI
GDP năm nay     = b₁×CPI năm trước   + b₂×GDP năm trước   + b₃×Lãi suất năm trước + b₄×Tỷ giá năm trước + sốc GDP
Lãi suất năm nay = c₁×CPI năm trước  + c₂×GDP năm trước   + c₃×Lãi suất năm trước + c₄×Tỷ giá năm trước + sốc Lãi suất
Tỷ giá năm nay  = d₁×CPI năm trước   + d₂×GDP năm trước   + d₃×Lãi suất năm trước + d₄×Tỷ giá năm trước + sốc Tỷ giá
```

Số "(1)" trong VAR(1) nghĩa là mô hình chỉ nhìn lại 1 năm trước. VAR(2) sẽ nhìn lại 2 năm, nhưng cần gấp đôi số tham số — không phù hợp với mẫu 27 quan sát.

Các hệ số a₁, a₂, a₃, a₄, b₁, b₂... được ước lượng bằng phương pháp OLS (bình phương tối thiểu) trên dữ liệu lịch sử.

#### "Sốc" là gì?

"Sốc" (innovation/shock) là phần **bất ngờ** — phần biến động mà mô hình không thể giải thích bằng các giá trị năm trước. Ví dụ: năm 2008, CPI tăng vọt lên 23% — phần tăng vượt dự báo chính là "sốc CPI".

FEVD chính là phân tích cú sốc của biến nào gây ra bao nhiêu % sai số dự báo CPI.

---

### 6.2 FEVD — Phân rã Phương sai

#### 10 kỳ có nghĩa là dự đoán trước 10 năm không?

**Không hẳn.** 10 kỳ ở đây không phải là dự báo giá trị CPI cho 10 năm tới. FEVD 10 kỳ trả lời một câu hỏi khác hoàn toàn:

> Nếu ta liên tục dự báo CPI cho 10 kỳ liên tiếp, thì **sai số dự báo tích lũy** đến từ đâu?

- **Kỳ 1:** Sai số dự báo CPI cho năm sau gần như 100% do chính cú sốc CPI — vì các cú sốc từ GDP, lãi suất, tỷ giá chưa có thời gian lan truyền.
- **Kỳ 3–5:** Nếu GDP hay tỷ giá thực sự ảnh hưởng lạm phát, phần đóng góp của chúng sẽ bắt đầu tăng lên.
- **Kỳ 10:** Bức tranh dài hạn — phản ánh cấu trúc ổn định của mối quan hệ giữa các biến.

Nhìn xu hướng từ Kỳ 1 đến Kỳ 10 mới có kết luận đáng tin — không nên chỉ nhìn một kỳ duy nhất.

#### FEVD hoạt động ở đoạn nào của mô hình?

FEVD được tính **sau khi** VAR đã ước lượng xong tất cả hệ số. Thứ tự:

1. VAR ước lượng hệ số (a₁, a₂, b₁, b₂...) → xong.
2. Từ hệ số đó, tính ma trận **Moving Average** — cho biết cú sốc ở mỗi biến lan truyền qua hệ thống như thế nào qua từng kỳ.
3. FEVD sử dụng ma trận Moving Average để phân rã: sai số dự báo CPI tại kỳ h đến từ cú sốc CPI bao nhiêu %, cú sốc GDP bao nhiêu %, cú sốc Lãi suất bao nhiêu %, cú sốc Tỷ giá bao nhiêu %.

#### Tác dụng đối với kết quả cuối cùng

FEVD là **bằng chứng trung tâm** và duy nhất để trả lời câu hỏi nghiên cứu:

- Nếu cột "Quán tính tự thân — CPI" chiếm tỷ trọng lớn (trên 80%) và ổn định qua 10 kỳ → **Bệnh tự miễn**.
- Nếu các cột GDP, Lãi suất, Tỷ giá cộng lại chiếm tỷ trọng lớn → **Tác nhân bên ngoài**.

#### Biểu đồ FEVD cột chồng 10 kỳ — Vẽ từ đâu?

Biểu đồ FEVD được vẽ từ bảng số liệu mà hàm `fevd()` trong thư viện statsmodels trả về. Cụ thể:

1. Sau khi `var_model.fit(1)` hoàn tất, gọi `var_model.fevd(10)` — yêu cầu statsmodels tính FEVD cho 10 kỳ.
2. Hàm này trả về một mảng 3 chiều: `(10 kỳ × 4 biến × 4 biến)` — trong đó mỗi dòng cho biết tỷ trọng đóng góp của từng biến vào sai số dự báo của từng biến khác tại kỳ đó.
3. Ta trích ra dòng của CPI — tức là chỉ lấy phần "sai số dự báo CPI được giải thích bởi từng biến".
4. Nhân với 100 để chuyển thành phần trăm.
5. Vẽ biểu đồ cột chồng (stacked bar chart) — mỗi cột là một kỳ, mỗi màu trong cột là tỷ trọng của một biến.

> 📷 **Chụp biểu đồ FEVD cột chồng 10 kỳ** từ trang VAR Model trên Streamlit. Đây là biểu đồ quan trọng nhất của toàn bộ đồ án.

---

## 7. Kiểm tra Phụ — Granger Causality

### 7.1 Granger Causality là gì?

Granger Causality — Nhân quả Granger — là kiểm định thống kê để trả lời câu hỏi:

> **Biết giá trị quá khứ của biến X có giúp dự báo biến Y tốt hơn không?**

Nếu có, ta nói "X Granger-cause Y" — tức là X có **tín hiệu dẫn dắt** Y. Lưu ý: đây không phải nhân quả theo nghĩa "X gây ra Y" — mà chỉ là "X xuất hiện trước và mang thông tin hữu ích để dự đoán Y".

Ví dụ: Nếu biết GDP năm trước tăng 8%, ta có dự báo CPI năm nay tốt hơn so với khi không biết thông tin GDP? Nếu câu trả lời là có, GDP Granger-cause CPI.

### 7.2 Cách đọc kết quả

Kiểm định Granger cho ra p-value:
- **p-value nhỏ hơn 0.05:** Có bằng chứng thống kê rằng biến đó dẫn dắt CPI.
- **p-value lớn hơn 0.05:** Không đủ bằng chứng rằng biến đó dẫn dắt CPI.

### 7.3 Tại sao phải kiểm tra Granger?

Granger Causality là **kiểm tra phụ** — nó bổ sung thêm bằng chứng cho kết luận từ FEVD:

- Nếu FEVD cho thấy GDP chỉ đóng góp 5% phương sai CPI, nhưng Granger lại cho thấy GDP **có** tín hiệu dẫn dắt → Điều này có nghĩa là GDP có ảnh hưởng thật nhưng mức độ nhỏ.
- Nếu FEVD cho thấy Tỷ giá đóng góp 3% và Granger cũng **không** tìm thấy tín hiệu dẫn dắt → Xác nhận thêm rằng tỷ giá không phải nguyên nhân chính.

Granger không thay đổi kết luận chính từ FEVD, nhưng giúp kết luận thêm vững chắc và đa chiều hơn.

> 📷 **Chụp bảng Granger Causality** từ trang VAR Model trên Streamlit.

---

## Tóm tắt

| Công cụ | Trả lời câu hỏi gì | Vai trò |
|:---|:---|:---|
| ADF Test | Chuỗi có dừng không? | Tiền đề bắt buộc cho VAR |
| Sai phân | Biến đổi chuỗi không dừng thành dừng | Tiền đề bắt buộc cho VAR |
| VIF | Các biến có trùng thông tin không? | Tiền đề bắt buộc cho VAR |
| VAR(1) | Các biến ảnh hưởng qua lại như thế nào? | Mô hình nền tảng |
| **FEVD 10 kỳ** | **Sai số dự báo CPI đến từ đâu?** | **Bằng chứng trung tâm** |
| Granger | Biến nào có tín hiệu dẫn dắt CPI? | Kiểm tra phụ |
| IRF | CPI phản ứng thế nào trước cú sốc? | Kiểm tra phụ |
