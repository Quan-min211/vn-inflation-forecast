import sys
from pathlib import Path

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils import fit_var_model, get_cpi_fevd, setup_page

setup_page("Conclusion", "✅")

st.title("Kết luận")

result, _, _, _ = fit_var_model()
fevd = get_cpi_fevd(result, periods=10)
cpi_col = "Quán tính tự thân (CPI)"
inertia_avg = fevd.loc["Kỳ 2":"Kỳ 10", cpi_col].mean()
external_avg = 100 - inertia_avg

st.markdown("""
## Câu hỏi

*Lạm phát tại Việt Nam chủ yếu là do "Bệnh tự miễn" (quán tính) hay "Tác nhân bên ngoài"?*
""")

col1, col2 = st.columns(2)
col1.metric("Quán tính CPI", f"{inertia_avg:.1f}%")
col2.metric("Tác nhân bên ngoài", f"{external_avg:.1f}%")

st.success(
    "Câu trả lời dựa trên dữ liệu: Lạm phát tại Việt Nam trong 3 thập kỷ qua "
    "chủ yếu mang tính QUÁN TÍNH (Bệnh tự miễn)."
)

st.markdown("""
## Chuỗi bằng chứng

1. **FEVD 10 kỳ**: CPI tự giải thích phần lớn sai số dự báo lạm phát.
2. **VAR(1)**: phù hợp với mẫu năm nhỏ và giữ tinh thần bản notebook cũ.
3. **Tác nhân bên ngoài**: GDP, lãi suất và tỷ giá có vai trò phụ, nhưng không áp đảo quán tính.

## Hàm ý

- Chính sách nên ưu tiên neo kỳ vọng lạm phát.
- Truyền thông chính sách cần ổn định và nhất quán.
- GDP/tỷ giá nên được theo dõi như tín hiệu phụ, không phải trung tâm kết luận.
""")
