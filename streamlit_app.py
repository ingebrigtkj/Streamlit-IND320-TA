import streamlit as st
import pandas as pd
import altair as alt

st.title("📊 CSV Viewer & Advanced Charts")

df = pd.read_csv("planets.csv")

st.subheader("Raw Data")
st.write(df)

numeric_cols = df.select_dtypes(include="number").columns

st.subheader("Each Column Separately")

for col in numeric_cols:
    st.write(f"### {col}")
    st.bar_chart(df[col])

st.subheader("All Columns Together (Split Y-Axis)")

if len(numeric_cols) > 1:
    melted_df = df.reset_index().melt("Name", value_vars=numeric_cols)

    chart = (
        alt.Chart(melted_df)
        .mark_line()
        .encode(
            x="Name",
            y=alt.Y("value", scale=alt.Scale(zero=False)),
            color="variable",
        )
        .properties(width=700, height=400)
    )

    st.altair_chart(chart, use_container_width=True)
else:
    st.info("Need at least 2 numeric columns to plot them together.")

st.subheader("Edit Data")
edited_df = st.data_editor(df, num_rows="dynamic")
st.write("Here’s your edited DataFrame:")
st.write(edited_df)
