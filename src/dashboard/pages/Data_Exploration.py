"""
Data Exploration — Chapter 2: Raw Data Characterization
"""
import streamlit as st
import sys
from pathlib import Path
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils import setup_page, load_raw_data, clean_data

# ---------------------------------------------------------------------------
setup_page("Data Exploration", "📊")
# ---------------------------------------------------------------------------

st.title("📊 Chương 2: Khám phá & Đặc trưng hóa Dữ liệu Thô")
st.info(
    "**Triết lý phân tích:** Trước khi đưa bất kỳ dữ liệu nào vào mô hình, "
    "chúng ta PHẢI hiểu rõ dữ liệu mình đang có. Mỗi biến số có những đặc điểm riêng "
    "(phân phối, xu hướng, giá trị thiếu) mà nếu không nắm bắt sẽ dẫn đến kết luận sai lệch.",
    icon="💡"
)

# ===== 2.1-2.3: Data Overview =====
st.markdown("## 2.1 – 2.3 Tổng quan Dữ liệu")

df_raw = load_raw_data()
df = clean_data()

tab_raw, tab_stats = st.tabs(["📋 Dữ liệu thô", "📊 Thống kê mô tả"])

with tab_raw:
    st.markdown(f"**Shape:** `{df_raw.shape[0]}` dòng × `{df_raw.shape[1]}` cột")
    st.dataframe(df_raw, use_container_width=True, height=400)

with tab_stats:
    st.markdown("Các thống kê cơ bản (mean, std, min, max) cho biết phạm vi và phân bố của từng biến:")
    st.dataframe(df_raw.describe().round(2), use_container_width=True)

# ===== 2.4: Missing Values =====
st.divider()
st.markdown("## 2.4 Phân tích Giá trị Thiếu (Missing Values)")

st.markdown("""
**Tại sao phải kiểm tra giá trị thiếu?**
- Dữ liệu kinh tế vĩ mô từ World Bank thường có khoảng trống do một số quốc gia chưa thống kê đầy đủ.
- Nếu bỏ qua missing values → mô hình sẽ bị lệch (biased) hoặc không thể chạy.
""")

missing_counts = df_raw.isnull().sum()
missing_pct = (missing_counts / len(df_raw)) * 100

col_heat, col_bar = st.columns(2)

with col_heat:
    st.markdown("#### Bản đồ Giá trị Thiếu")
    missing_matrix = df_raw.drop(columns=['years'], errors='ignore').isnull().astype(int)
    fig_heat = px.imshow(
        missing_matrix.T,
        color_continuous_scale=["#1B3A4B", "#FFD700"],
        labels=dict(x="Chỉ số dòng (Năm)", y="Biến", color="Missing"),
        aspect="auto"
    )
    fig_heat.update_layout(
        title="Vàng = Giá trị thiếu",
        height=400,
        coloraxis_showscale=False
    )
    st.plotly_chart(fig_heat, use_container_width=True)

with col_bar:
    st.markdown("#### Tỷ lệ % Giá trị Thiếu")
    missing_filtered = missing_pct[missing_pct > 0]
    if len(missing_filtered) > 0:
        fig_bar = px.bar(
            x=missing_filtered.values,
            y=missing_filtered.index,
            orientation='h',
            labels={'x': '% Missing', 'y': 'Biến'},
            color_discrete_sequence=['#FF6B6B']
        )
        fig_bar.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.success("Không có giá trị thiếu!")

st.warning(
    "**Nhận xét:** `domestic_credit_index` và `lending_interest_percent` (Trụ cột Tiền tệ) có giá trị thiếu. "
    "**Giải pháp:** Nội suy tuyến tính (Linear Interpolation) — phù hợp cho dữ liệu chuỗi thời gian.",
    icon="⚠️"
)

# ===== 2.5: Data Cleaning Summary =====
st.divider()
st.markdown("## 2.5 Làm sạch Dữ liệu")

col_before, col_after = st.columns(2)
with col_before:
    st.metric("Giá trị thiếu TRƯỚC xử lý", f"{df_raw.isnull().sum().sum()}")
with col_after:
    st.metric("Giá trị thiếu SAU xử lý", f"{df.isnull().sum().sum()}", delta="0 ✓", delta_color="off")

with st.expander("🔧 Chi tiết: Phát hiện cột trùng lặp"):
    st.markdown("""
    - Cột `gdp_delflator_percent` (lỗi chính tả) thực chất là **GDP Deflator INDEX** (chỉ số tích lũy).
    - Cột `gdp_deflator_percent` là **GDP Deflator GROWTH RATE** (tỷ lệ % thay đổi).
    - **Hành động:** Đổi tên cột lỗi thành `gdp_deflator_index` để phân biệt rõ ràng.
    """)

# ===== 2.6: Time Series Trends =====
st.divider()
st.markdown("## 2.6 Xu hướng theo Thời gian — Bảng điều khiển Kinh tế Vĩ mô")

st.markdown("""
**Mục đích:** Trước khi chạy bất kỳ model nào, ta cần "nhìn" dữ liệu bằng mắt:
1. Phát hiện các sự kiện kinh tế lớn.
2. Nhận biết chuỗi có "dừng" (stationary) hay không.
3. Tìm mối liên hệ trực quan giữa các biến.
""")

fig_trends = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        "1. Lạm phát bùng nổ trùng với khủng hoảng toàn cầu",
        "2. Chính sách tiền tệ phản chu kỳ: Hạ lãi suất → Tín dụng tăng",
        "3. Chuyển đổi: Thâm hụt → Thặng dư bền vững sau 2012",
        "4. GDP dài hạn bền bỉ, suy giảm chu kỳ hậu COVID"
    ),
    vertical_spacing=0.12,
    horizontal_spacing=0.08,
    specs=[[{}, {"secondary_y": True}], [{}, {}]]
)

years = df.index

fig_trends.add_trace(
    go.Scatter(x=years, y=df['cpi_growth_percent'], mode='lines',
               line=dict(color='#E24A33', width=3), name='CPI Growth Rate',
               fill='tozeroy', fillcolor='rgba(226,74,51,0.1)'),
    row=1, col=1
)
fig_trends.add_vrect(x0="2008-01-01", x1="2009-12-31", fillcolor="gray",
                     opacity=0.15, line_width=0, row=1, col=1,
                     annotation_text="Khủng hoảng 2008", annotation_position="top left",
                     annotation_font_size=9)
fig_trends.add_vrect(x0="2020-01-01", x1="2021-12-31", fillcolor="blue",
                     opacity=0.1, line_width=0, row=1, col=1,
                     annotation_text="COVID-19", annotation_position="top right",
                     annotation_font_size=9)

fig_trends.add_trace(
    go.Scatter(x=years, y=df['domestic_credit_index'].ffill(), mode='lines',
               line=dict(color='#348ABD', width=2.5), name='Credit Index (Trái)'),
    row=1, col=2, secondary_y=False
)
fig_trends.add_trace(
    go.Scatter(x=years, y=df['lending_interest_percent'].ffill(), mode='lines',
               line=dict(color='#988ED5', width=2.5, dash='dash'), name='Lending Rate (Phải)'),
    row=1, col=2, secondary_y=True
)

fig_trends.add_trace(
    go.Scatter(x=years, y=df['export_index'], mode='lines',
               line=dict(color='#FBC15E', width=2.5), name='Export Index'),
    row=2, col=1
)
fig_trends.add_trace(
    go.Scatter(x=years, y=df['import_index'], mode='lines',
               line=dict(color='#8EBA42', width=2.5), name='Import Index'),
    row=2, col=1
)

fig_trends.add_trace(
    go.Bar(x=years, y=df['gdp_growth_percent'].ffill(),
           marker_color='#4682B4', opacity=0.4, name='GDP Growth (Bar)'),
    row=2, col=2
)
fig_trends.add_trace(
    go.Scatter(x=years, y=df['gdp_growth_percent'].ffill(), mode='lines+markers',
               line=dict(color='#4682B4', width=2.5), marker=dict(size=5),
               name='GDP Trend (Line)'),
    row=2, col=2
)

fig_trends.update_layout(
    height=750,
    title_text="BẢNG ĐIỀU KHIỂN KINH TẾ VĨ MÔ VIỆT NAM (1996–2022)",
    title_font_size=18,
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=-0.12, xanchor="center", x=0.5,
                font=dict(size=10)),
    template="plotly_white"
)

fig_trends.update_yaxes(title_text="Inflation Rate (%)", row=1, col=1)
fig_trends.update_yaxes(title_text="Credit Index", secondary_y=False, row=1, col=2)
fig_trends.update_yaxes(title_text="Lending Rate (%)", secondary_y=True, row=1, col=2)
fig_trends.update_yaxes(title_text="Value Index", row=2, col=1)
fig_trends.update_yaxes(title_text="GDP Growth Rate (%)", row=2, col=2)

st.plotly_chart(fig_trends, use_container_width=True)

# ===== Annotations =====
st.markdown("### 📝 Nhận xét từ Biểu đồ Xu hướng")

col_n1, col_n2 = st.columns(2)

with col_n1:
    st.markdown("""
    **1. Lạm phát (CPI Growth):**
    Hai đỉnh lạm phát lớn nhất (2008 và 2011) trùng với khủng hoảng tài chính toàn cầu
    và chính sách tiền tệ nới lỏng trong nước → lạm phát VN chịu tác động từ CẢ
    yếu tố nội sinh lẫn ngoại sinh.

    **2. Tín dụng vs Lãi suất:**
    Mối quan hệ nghịch rõ rệt — khi lãi suất giảm, tín dụng tăng vọt.
    Đây là cơ chế truyền dẫn tiền tệ cổ điển.
    """)

with col_n2:
    st.markdown("""
    **3. Import/Export:**
    Việt Nam chuyển từ thâm hụt thương mại sang thặng dư bền vững sau 2012,
    nhờ hội nhập sâu vào chuỗi cung ứng toàn cầu (FDI từ Samsung, Intel...).

    **4. GDP:**
    Tăng trưởng ổn định 5–7% với duy nhất 2020 suy giảm mạnh do COVID-19.
    """)

st.error(
    "**Kết luận quan trọng:** Các chuỗi Index (CPI Index, Credit Index, Exchange Rate) "
    "có xu hướng tăng liên tục → chắc chắn **KHÔNG dừng**. Điều này buộc ta phải "
    "**lấy sai phân (differencing)** trước khi đưa vào VAR ở Chương 4.",
    icon="🚨"
)
