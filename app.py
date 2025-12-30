# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# # Page config
# st.set_page_config(
#     page_title="CIMB Digital Products Comparison",
#     page_icon="🏦",
#     layout="wide"
# )

# # Custom CSS
# st.markdown("""
# <style>
#     .main-header {
#         font-size: 3rem;
#         font-weight: bold;
#         text-align: center;
#         color: #DC2626;
#         margin-bottom: 0.5rem;
#     }
#     .sub-header {
#         font-size: 1.2rem;
#         text-align: center;
#         color: #6B7280;
#         margin-bottom: 2rem;
#     }
#     .metric-card {
#         background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#         padding: 1.5rem;
#         border-radius: 10px;
#         color: white;
#         text-align: center;
#     }
#     .product-card {
#         padding: 1rem;
#         border-radius: 8px;
#         border-left: 4px solid;
#         background: white;
#         margin-bottom: 0.5rem;
#         box-shadow: 0 1px 3px rgba(0,0,0,0.1);
#     }
#     .common { border-color: #10B981; }
#     .personal { border-color: #DC2626; }
#     .branchless { border-color: #F59E0B; }
# </style>
# """, unsafe_allow_html=True)

# # Data produk digital
# common_products = [
#     'Aplikasi OCTO (OCTO Mobile)',
#     'Website OCTO (OCTO Clicks)',
#     'OCTO Pay',
#     'OCTO Chat',
#     'OCTO Merchant',
#     'Digital Lounge'
# ]

# personal_only = [
#     'OCTO Savers',
#     'OCTO Cash',
#     'BizChannel@CIMB',
#     'BizChannel@CIMB Mobile',
#     'Remittance'
# ]

# branchless_only = [
#     'OCTO Vending',
#     'ATM CIMB Niaga'
# ]

# # Header
# st.markdown('<div class="main-header">🏦 CIMB Niaga Digital Products</div>', unsafe_allow_html=True)
# st.markdown('<div class="sub-header">Comparison: Personal Banking vs Branchless Banking</div>', unsafe_allow_html=True)

# # Stats
# stats = {
#     'Personal Banking': len(common_products) + len(personal_only),
#     'Branchless Banking': len(common_products) + len(branchless_only),
#     'Ada di Keduanya': len(common_products),
#     'Personal Only': len(personal_only),
#     'Branchless Only': len(branchless_only)
# }

# # Display stats in columns
# col1, col2, col3, col4, col5 = st.columns(5)

# with col1:
#     st.metric("Personal Banking", stats['Personal Banking'], delta=None)
# with col2:
#     st.metric("Branchless Banking", stats['Branchless Banking'], delta=None)
# with col3:
#     st.metric("Ada di Keduanya", stats['Ada di Keduanya'], delta=None)
# with col4:
#     st.metric("Personal Only", stats['Personal Only'], delta=None)
# with col5:
#     st.metric("Branchless Only", stats['Branchless Only'], delta=None)

# st.markdown("---")

# # Visualizations
# col_left, col_right = st.columns(2)

# with col_left:
#     st.subheader("📊 Distribusi Produk")
    
#     # Pie chart
#     fig_pie = go.Figure(data=[go.Pie(
#         labels=['Ada di Keduanya', 'Personal Only', 'Branchless Only'],
#         values=[len(common_products), len(personal_only), len(branchless_only)],
#         marker_colors=['#10B981', '#DC2626', '#F59E0B'],
#         hole=0.4
#     )])
#     fig_pie.update_layout(height=400, showlegend=True)
#     st.plotly_chart(fig_pie, use_container_width=True)

# with col_right:
#     st.subheader("📈 Perbandingan Total")
    
#     # Bar chart
#     df_bar = pd.DataFrame({
#         'Platform': ['Personal Banking', 'Branchless Banking'],
#         'Jumlah Produk': [stats['Personal Banking'], stats['Branchless Banking']]
#     })
    
#     fig_bar = px.bar(
#         df_bar, 
#         x='Platform', 
#         y='Jumlah Produk',
#         color='Platform',
#         color_discrete_map={
#             'Personal Banking': '#DC2626',
#             'Branchless Banking': '#F59E0B'
#         }
#     )
#     fig_bar.update_layout(height=400, showlegend=False)
#     st.plotly_chart(fig_bar, use_container_width=True)

# st.markdown("---")

# # Search & Filter
# st.subheader("🔍 Cari & Filter Produk")

# col_search, col_filter = st.columns([3, 2])

# with col_search:
#     search_term = st.text_input("Cari produk digital...", "", placeholder="Ketik nama produk...")

# with col_filter:
#     filter_option = st.selectbox(
#         "Filter berdasarkan:",
#         ["Semua Produk", "Ada di Keduanya", "Personal Only", "Branchless Only"]
#     )

# st.markdown("---")

# # Create DataFrame
# all_products = []

# for product in common_products:
#     all_products.append({
#         'Produk': product,
#         'Kategori': 'Ada di Keduanya',
#         'Type': 'common'
#     })

# for product in personal_only:
#     all_products.append({
#         'Produk': product,
#         'Kategori': 'Personal Only',
#         'Type': 'personal'
#     })

# for product in branchless_only:
#     all_products.append({
#         'Produk': product,
#         'Kategori': 'Branchless Only',
#         'Type': 'branchless'
#     })

# df = pd.DataFrame(all_products)

# # Apply filters
# if search_term:
#     df = df[df['Produk'].str.contains(search_term, case=False)]

# if filter_option != "Semua Produk":
#     df = df[df['Kategori'] == filter_option]

# # Display products in 3 columns
# if len(df) > 0:
#     # Group by category
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         st.subheader("🟢 Ada di Keduanya")
#         common_df = df[df['Type'] == 'common']
#         for _, row in common_df.iterrows():
#             st.markdown(f"""
#             <div class="product-card common">
#                 <strong>{row['Produk']}</strong><br>
#                 <span style="color: #10B981; font-size: 0.9rem;">✓ Ada di Keduanya</span>
#             </div>
#             """, unsafe_allow_html=True)
    
#     with col2:
#         st.subheader("🔴 Personal Only")
#         personal_df = df[df['Type'] == 'personal']
#         for _, row in personal_df.iterrows():
#             st.markdown(f"""
#             <div class="product-card personal">
#                 <strong>{row['Produk']}</strong><br>
#                 <span style="color: #DC2626; font-size: 0.9rem;">✓ Personal Banking</span>
#             </div>
#             """, unsafe_allow_html=True)
    
#     with col3:
#         st.subheader("🟠 Branchless Only")
#         branchless_df = df[df['Type'] == 'branchless']
#         for _, row in branchless_df.iterrows():
#             st.markdown(f"""
#             <div class="product-card branchless">
#                 <strong>{row['Produk']}</strong><br>
#                 <span style="color: #F59E0B; font-size: 0.9rem;">✓ Branchless Banking</span>
#             </div>
#             """, unsafe_allow_html=True)
    
#     st.markdown("---")
    
#     # Data table
#     st.subheader("📋 Tabel Detail")
#     st.dataframe(
#         df[['Produk', 'Kategori']],
#         use_container_width=True,
#         hide_index=True
#     )
    
#     # Download button
#     csv = df.to_csv(index=False, encoding='utf-8-sig')
#     st.download_button(
#         label="📥 Download CSV",
#         data=csv,
#         file_name="cimb_digital_products.csv",
#         mime="text/csv"
#     )

# else:
#     st.warning("⚠️ Tidak ada produk yang cocok dengan pencarian Anda")

# # Footer
# st.markdown("---")
# st.subheader("💡 Kesimpulan")

# col_a, col_b = st.columns(2)

# with col_a:
#     st.success(f"""
#     **Personal Banking** lebih lengkap dengan **{stats['Personal Banking']} produk digital**, 
#     termasuk produk corporate (BizChannel) dan layanan remittance internasional.
#     """)

# with col_b:
#     st.info(f"""
#     **Branchless Banking** fokus ke consumer dengan **{stats['Branchless Banking']} produk**, 
#     memiliki fitur unik seperti OCTO Vending.
#     """)

# st.markdown(f"""
# <div style="background: #F3F4F6; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
#     <strong>📊 Ringkasan:</strong> Terdapat <strong>{stats['Ada di Keduanya']} produk digital</strong> 
#     yang tersedia di kedua platform, menunjukkan integrasi yang baik antara kedua channel.
# </div>
# """, unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="CIMB Digital Products",
    page_icon="🏦",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("products.csv")

df = load_data()

# ===== HEADER =====
st.markdown("<h1 style='text-align:center;color:#DC2626'>🏦 CIMB Niaga Digital Products</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray'>Personal Banking vs Branchless Banking</p>", unsafe_allow_html=True)

# ===== STATS =====
stats = {
    "Personal Banking": len(df[df["Type"].isin(["common", "personal"])]),
    "Branchless Banking": len(df[df["Type"].isin(["common", "branchless"])]),
    "Ada di Keduanya": len(df[df["Type"] == "common"]),
    "Personal Only": len(df[df["Type"] == "personal"]),
    "Branchless Only": len(df[df["Type"] == "branchless"])
}

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Personal Banking", stats["Personal Banking"])
c2.metric("Branchless Banking", stats["Branchless Banking"])
c3.metric("Ada di Keduanya", stats["Ada di Keduanya"])
c4.metric("Personal Only", stats["Personal Only"])
c5.metric("Branchless Only", stats["Branchless Only"])

st.divider()

# ===== CHARTS =====
col1, col2 = st.columns(2)

with col1:
    fig_pie = go.Figure(go.Pie(
        labels=["Ada di Keduanya", "Personal Only", "Branchless Only"],
        values=[
            stats["Ada di Keduanya"],
            stats["Personal Only"],
            stats["Branchless Only"]
        ],
        hole=0.4
    ))
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    df_bar = pd.DataFrame({
        "Platform": ["Personal Banking", "Branchless Banking"],
        "Jumlah Produk": [
            stats["Personal Banking"],
            stats["Branchless Banking"]
        ]
    })
    fig_bar = px.bar(df_bar, x="Platform", y="Jumlah Produk", color="Platform")
    st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

# ===== SEARCH & FILTER =====
search = st.text_input("🔍 Cari produk")
filter_opt = st.selectbox(
    "Filter",
    ["Semua Produk", "Ada di Keduanya", "Personal Only", "Branchless Only"]
)

filtered = df.copy()

if search:
    filtered = filtered[filtered["Produk"].str.contains(search, case=False)]

if filter_opt != "Semua Produk":
    filtered = filtered[filtered["Kategori"] == filter_opt]

# ===== DISPLAY =====
c1, c2, c3 = st.columns(3)

with c1:
    st.subheader("🟢 Ada di Keduanya")
    for p in filtered[filtered["Type"] == "common"]["Produk"]:
        st.success(p)

with c2:
    st.subheader("🔴 Personal Only")
    for p in filtered[filtered["Type"] == "personal"]["Produk"]:
        st.error(p)

with c3:
    st.subheader("🟠 Branchless Only")
    for p in filtered[filtered["Type"] == "branchless"]["Produk"]:
        st.warning(p)

st.divider()

st.dataframe(filtered, use_container_width=True)

st.download_button(
    "📥 Download CSV",
    filtered.to_csv(index=False, encoding="utf-8-sig"),
    "cimb_digital_products.csv",
    "text/csv"
)
