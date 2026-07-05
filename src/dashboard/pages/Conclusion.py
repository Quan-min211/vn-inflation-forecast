"""
Conclusion — Chapter 6: The Ultimate Question Verdict
"""
import streamlit as st
import sys
from pathlib import Path
import pandas as pd
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils import setup_page, fit_var_model, VAR_LABELS_VN

# ---------------------------------------------------------------------------
setup_page("Conclusion", "📋")
# ---------------------------------------------------------------------------

st.title("📋 Chương 6: Kết luận — Trả lời Câu hỏi Tối thượng")
st.divider()

var_result, optimal_lag, var_data = fit_var_model()
fevd = var_result.fevd(10)
cpi_idx = list(var_data.columns).index('cpi_growth_percent')
fevd_cpi = fevd.decomp[:, cpi_idx, :] * 100
labels = [VAR_LABELS_VN.get(c, c) for c in var_data.columns]

cpi_avg = fevd_cpi[1:, cpi_idx].mean()
external_avg = 100 - cpi_avg

st.markdown("## 6.1 Bảng Tổng kết Bằng chứng")

evidence_data = {
    "Tiêu chí": [
        "Mô hình sử dụng",
        "Câu hỏi 1: Quán tính có mạnh không?",
        "Câu hỏi 2: Yếu tố ngoại sinh nào đáng kể?",
        "Impulse Response Function (IRF)",
        "Kết luận tổng thể"
    ],
    "Kết quả từ Mô hình VAR": [
        "CPI + GDP + Tỷ giá + Lãi suất (Vector Autoregression)",
        f"FEVD: CPI tự giải thích ~{cpi_avg:.0f}% biến động → Quán tính áp đảo",
        f"Granger Causality: Chỉ 1–2 biến dẫn dắt yếu (<{external_avg:.0f}% phương sai)",
        "Cú sốc từ biến ngoại sinh tắt dần nhanh → ảnh hưởng ngắn hạn",
        '✅ "Bệnh tự miễn" — Quán tính là động lực CHÍNH của lạm phát VN'
    ]
}
st.dataframe(pd.DataFrame(evidence_data), use_container_width=True, hide_index=True)

st.divider()
st.markdown("## 6.2 Phán quyết: Trả lời The Ultimate Question")

st.markdown("""
> **"Lạm phát tại Việt Nam chủ yếu là do 'Bệnh tự miễn' (Quán tính kỳ vọng)
> hay 'Tác nhân bên ngoài' (Tỷ giá, Tín dụng, GDP)?"**
""")

st.markdown(f"""
<div style="background: linear-gradient(135deg, #1B3A4B 0%, #2C5F7C 100%);
            color: white; padding: 2rem; border-radius: 16px;
            text-align: center; margin: 1rem 0;">
    <h2 style="color: #FFD700; margin-bottom: 0.5rem;">🏆 CÂU TRẢ LỜI DỰA TRÊN DỮ LIỆU</h2>
    <h3 style="color: white; margin-bottom: 1rem;">
        Lạm phát tại Việt Nam trong 3 thập kỷ qua chủ yếu mang tính<br>
        <span style="color: #FFD700; font-size: 1.8rem;">QUÁN TÍNH (Bệnh tự miễn)</span>
    </h3>
    <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 1.5rem;">
        <div style="background: rgba(255,255,255,0.15); padding: 1rem; border-radius: 10px;">
            <div style="font-size: 2.5rem; font-weight: bold; color: #FFD700;">{cpi_avg:.1f}%</div>
            <div style="font-size: 0.9rem;">Quán tính CPI</div>
        </div>
        <div style="background: rgba(255,255,255,0.15); padding: 1rem; border-radius: 10px;">
            <div style="font-size: 2.5rem; font-weight: bold; color: #2EC4B6;">{external_avg:.1f}%</div>
            <div style="font-size: 0.9rem;">Yếu tố ngoại sinh</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("### 📐 Chuỗi Bằng chứng")
st.markdown(f"""
**1. Phân rã phương sai (FEVD):** ~{cpi_avg:.0f}% biến động lạm phát do quán tính, không phải GDP/Tỷ giá/Lãi suất.

**2. Granger Causality:** Chỉ GDP có tín hiệu dẫn dắt, đóng góp rất nhỏ. Lãi suất là **phản ứng chính sách**.

**3. IRF:** Phản ứng CPI trước cú sốc ngoại sinh tắt dần nhanh (2–3 kỳ) → ảnh hưởng nhất thời.
""")

st.markdown("### 🔄 Cơ chế Kinh tế: Vòng lặp Kỳ vọng")
st.markdown("""
<div style="background: #FFF3E0; padding: 1.5rem; border-radius: 12px; border-left: 5px solid #FF9800;">
    <p style="font-size: 1.1rem; line-height: 1.8;">
        Kỳ vọng giá tăng → đẩy giá bán lên trước → giá thực sự tăng → xác nhận kỳ vọng → vòng lặp tiếp tục.
    </p>
    <p style="font-size: 0.9rem; color: #666;">
        "Bệnh tự miễn" — hệ miễn dịch (kỳ vọng) tấn công chính cơ thể (nền kinh tế).
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()
st.markdown("## 6.3 Hàm ý Chính sách")

col_p1, col_p2, col_p3 = st.columns(3)
with col_p1:
    st.markdown("""
    <div style="background: linear-gradient(180deg, #E8F5E9, #C8E6C9);
                padding: 1.5rem; border-radius: 12px; height: 100%;">
        <h4>🎯 Neo Kỳ vọng Lạm phát</h4>
        <p>NHNN công bố mục tiêu lạm phát rõ ràng, giữ cam kết.</p>
        <p style="font-size: 0.8rem; color: #666;"><strong>Ưu tiên:</strong> Cao nhất</p>
    </div>
    """, unsafe_allow_html=True)
with col_p2:
    st.markdown("""
    <div style="background: linear-gradient(180deg, #E3F2FD, #BBDEFB);
                padding: 1.5rem; border-radius: 12px; height: 100%;">
        <h4>📢 Truyền thông Minh bạch</h4>
        <p>Giải thích minh bạch quyết định tiền tệ → giảm bất định.</p>
        <p style="font-size: 0.8rem; color: #666;"><strong>Ưu tiên:</strong> Cao</p>
    </div>
    """, unsafe_allow_html=True)
with col_p3:
    st.markdown("""
    <div style="background: linear-gradient(180deg, #FFF3E0, #FFE0B2);
                padding: 1.5rem; border-radius: 12px; height: 100%;">
        <h4>📈 Giám sát GDP</h4>
        <p>GDP là kênh ngoại sinh duy nhất đáng kể. Phát hiện sớm overheating.</p>
        <p style="font-size: 0.8rem; color: #666;"><strong>Ưu tiên:</strong> Trung bình</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.markdown("## 6.4 Hạn chế & Hướng Phát triển")

col_lim, col_fut = st.columns(2)
with col_lim:
    st.markdown("### ⚠️ Hạn chế")
    st.markdown("""
    - **Kích thước mẫu nhỏ:** 27 quan sát → giảm sức mạnh thống kê.
    - **Tần suất thấp:** Dữ liệu năm → bỏ lỡ biến động tháng/quý.
    - **Giả định tuyến tính:** VAR khó bắt structural breaks.
    - **Chưa kiểm chứng ngoài mẫu.**
    """)
with col_fut:
    st.markdown("### 🚀 Hướng Phát triển")
    st.markdown("""
    - Dữ liệu **tháng/quý** từ GSO → hàng trăm quan sát.
    - **Structural VAR** với ràng buộc kinh tế.
    - **ML:** LSTM, Random Forest cho phi tuyến.
    - **ARIMA** đơn biến: so sánh quán tính vs. đa biến.
    - **NLP Sentiment** trên báo chí kinh tế VN.
    """)

st.divider()
st.markdown("""
<div style="text-align: center; padding: 1rem; color: #888;">
    <p><strong>Nhóm 02</strong> — Phân tích Dữ liệu — DAAN436277_02</p>
    <p>GVHD: ThS. Trần Trọng Bình | HCMUTE</p>
</div>
""", unsafe_allow_html=True)
