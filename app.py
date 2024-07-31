
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the Excel file
# excel_file = "ESG.xlsx"
# df_excel = pd.read_excel(excel_file)

# # Required columns for comparison
# required_columns = ["Company", "Greenhouse gas emissions (tonnes CO2e)", "Energy usage (MWh)", "Water usage (cubic meters)"]

# # Ensure the required columns are in the DataFrame
# for col in required_columns:
#     if col not in df_excel.columns:
#         st.error(f"Column '{col}' not found in the Excel file. Please check the file.")
#         st.stop()

# # Streamlit app
# st.title("ESG Data Input and Visualization")

# # Input fields for user to add new data
# st.header("Input New Data")
# new_data = {
#     "Rank": st.number_input("Rank", min_value=1, value=1, step=1, key="rank_input"),
#     "Company": st.text_input("Company", key="company_input"),
#     "Region": st.text_input("Region", key="region_input"),
#     "Country": st.text_input("Country", key="country_input"),
#     "Sector": st.text_input("Sector", key="sector_input"),
#     "Industry": st.text_input("Industry", key="industry_input"),
#     "ESG Score": st.number_input("ESG Score", min_value=0, max_value=100, value=50, step=1, key="esg_score_input"),
#     "Temperature Score (2050)": st.number_input("Temperature Score (2050)", min_value=0.0, max_value=5.0, value=2.0, step=0.1, key="temp_score_input"),
#     "Emissions: Tonnes of CO2e (Scope 1 & 2)": st.number_input("Emissions: Tonnes of CO2e (Scope 1 & 2)", min_value=0, value=1000, step=100, key="emissions_scope1_2_input"),
#     "Emissions: Tonnes of CO2e (Scope 3)": st.number_input("Emissions: Tonnes of CO2e (Scope 3)", min_value=0, value=1000, step=100, key="emissions_scope3_input"),
#     "Market Cap Category": st.text_input("Market Cap Category", key="market_cap_category_input"),
#     "E": st.number_input("E (Environmental Score)", min_value=0, max_value=100, value=20, step=1, key="e_input"),
#     "S": st.number_input("S (Social Score)", min_value=0, max_value=100, value=50, step=1, key="s_input"),
#     "G": st.number_input("G (Governance Score)", min_value=0, max_value=100, value=50, step=1, key="g_input"),
#     "DEI Labor Practices": st.number_input("DEI Labor Practices", min_value=0, value=100, step=10, key="dei_labor_practices_input"),
#     "Community Management": st.number_input("Community Management", min_value=0, value=100, step=10, key="community_management_input"),
#     "Board Diversity": st.number_input("Board Diversity", min_value=0, value=100, step=10, key="board_diversity_input"),
#     "Executive Compensation": st.number_input("Executive Compensation", min_value=0, value=100, step=10, key="executive_compensation_input"),
#     "Ethics and Compliance": st.number_input("Ethics and Compliance", min_value=0, value=100, step=10, key="ethics_compliance_input"),
#     "Greenhouse gas emissions (tonnes CO2e)": st.number_input("Greenhouse gas emissions (tonnes CO2e)", min_value=0, value=100, step=10, key="ghg_emissions_input"),
#     "Energy usage (MWh)": st.number_input("Energy usage (MWh)", min_value=0, value=100, step=10, key="energy_usage_input"),
#     "Water usage (cubic meters)": st.number_input("Water usage (cubic meters)", min_value=0, value=100, step=10, key="water_usage_input"),
# }

# # Add new data to DataFrame
# if st.button("Add Data", key="add_data_button"):
#     df_excel = pd.concat([df_excel, pd.DataFrame([new_data])], ignore_index=True)
#     df_excel.to_excel(excel_file, index=False)  # Save updated DataFrame to Excel
#     st.success("Data added successfully!")

# # Input fields for filtering data
# st.header("Filter Data")
# selected_sector = st.selectbox("Select Sector", df_excel["Sector"].unique(), key="sector_filter")
# selected_industry = st.selectbox("Select Industry", df_excel["Industry"].unique(), key="industry_filter")

# # Filter DataFrame based on user inputs
# filtered_df = df_excel[(df_excel["Sector"] == selected_sector) & (df_excel["Industry"] == selected_industry)]

# # Display filtered DataFrame
# st.header("Filtered ESG Data")
# st.dataframe(filtered_df)

# # Get the lowest E value of the filtered companies
# lowest_e_value = filtered_df["E"].min()

# # Check if the user's E value is lower than the lowest of the filtered companies
# if new_data["E"] < lowest_e_value:
#     st.warning("The Environmental Score (E) of your input is lower than the lowest E score of the filtered companies.")

#     # Compare the E factors of each company and the user's input
#     comparison_df = filtered_df[required_columns].copy()
#     user_row = pd.Series({
#         "Company": "Your Input",
#         "Greenhouse gas emissions (tonnes CO2e)": new_data["Greenhouse gas emissions (tonnes CO2e)"],
#         "Energy usage (MWh)": new_data["Energy usage (MWh)"],
#         "Water usage (cubic meters)": new_data["Water usage (cubic meters)"]
#     })
#     comparison_df = pd.concat([comparison_df, pd.DataFrame([user_row])], ignore_index=True)

#     # Display comparison DataFrame
#     st.header("Comparison of E Factors")
#     st.dataframe(comparison_df)

#     # Plot comparison charts
#     fig, axes = plt.subplots(3, 1, figsize=(10, 15))
#     comparison_df.set_index("Company")[["Greenhouse gas emissions (tonnes CO2e)"]].plot(kind="bar", ax=axes[0], color=['blue' if x != 'Your Input' else 'red' for x in comparison_df["Company"]])
#     axes[0].set_title("Greenhouse Gas Emission")
#     comparison_df.set_index("Company")[["Energy usage (MWh)"]].plot(kind="bar", ax=axes[1], color=['blue' if x != 'Your Input' else 'red' for x in comparison_df["Company"]])
#     axes[1].set_title("Energy Usage")
#     comparison_df.set_index("Company")[["Water usage (cubic meters)"]].plot(kind="bar", ax=axes[2], color=['blue' if x != 'Your Input' else 'red' for x in comparison_df["Company"]])
#     axes[2].set_title("Water Usage")
#     st.pyplot(fig)

# # Visualization section
# st.header("Visualization")

# # Select the type of plot
# plot_type = st.selectbox("Select Plot Type", ["Bar Chart", "Line Chart", "Area Chart"], key="plot_type")

# # Select columns to plot
# columns_to_plot = st.multiselect("Select Columns to Plot", df_excel.columns.tolist(), default=["ESG Score"], key="columns_to_plot")

# # Generate plots based on user selection
# if plot_type == "Bar Chart":
#     st.bar_chart(filtered_df[columns_to_plot])
# elif plot_type == "Line Chart":
#     st.line_chart(filtered_df[columns_to_plot])
# elif plot_type == "Area Chart":
#     st.area_chart(filtered_df[columns_to_plot])

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the Excel file
# excel_file = "ESG.xlsx"
# df_excel = pd.read_excel(excel_file)

# # Required columns for comparison
# required_columns = ["Company", "Greenhouse gas emissions (tonnes CO2e)", "Energy usage (MWh)", "Water usage (cubic meters)"]

# # Ensure the required columns are in the DataFrame
# for col in required_columns:
#     if col not in df_excel.columns:
#         st.error(f"Column '{col}' not found in the Excel file. Please check the file.")
#         st.stop()

# # Streamlit app
# st.title("ESG Data Input and Visualization")

# # Input fields for user to add new data
# new_data = {
#     "Rank": st.number_input("Rank", min_value=1, value=1, step=1, key="rank_input"),
#     "Company": st.text_input("Company", key="company_input"),
#     "Region": st.text_input("Region", key="region_input"),
#     "Country": st.text_input("Country", key="country_input"),
#     "Sector": "",  # Removed from input
#     "Industry": "",  # Removed from input
#     "ESG Score": st.number_input("ESG Score", min_value=0, max_value=100, value=50, step=1, key="esg_score_input"),
#     "Temperature Score (2050)": st.number_input("Temperature Score (2050)", min_value=0.0, max_value=5.0, value=2.0, step=0.1, key="temp_score_input"),
#     "Emissions: Tonnes of CO2e (Scope 1 & 2)": st.number_input("Emissions: Tonnes of CO2e (Scope 1 & 2)", min_value=0, value=1000, step=100, key="emissions_scope1_2_input"),
#     "Emissions: Tonnes of CO2e (Scope 3)": st.number_input("Emissions: Tonnes of CO2e (Scope 3)", min_value=0, value=1000, step=100, key="emissions_scope3_input"),
#     "Market Cap Category": st.text_input("Market Cap Category", key="market_cap_category_input"),
#     "E": st.number_input("E (Environmental Score)", min_value=0, max_value=100, value=20, step=1, key="e_input"),
#     "S": st.number_input("S (Social Score)", min_value=0, max_value=100, value=50, step=1, key="s_input"),
#     "G": st.number_input("G (Governance Score)", min_value=0, max_value=100, value=50, step=1, key="g_input"),
#     "DEI Labor Practices": st.number_input("DEI Labor Practices", min_value=0, value=100, step=10, key="dei_labor_practices_input"),
#     "Community Management": st.number_input("Community Management", min_value=0, value=100, step=10, key="community_management_input"),
#     "Board Diversity": st.number_input("Board Diversity", min_value=0, value=100, step=10, key="board_diversity_input"),
#     "Executive Compensation": st.number_input("Executive Compensation", min_value=0, value=100, step=10, key="executive_compensation_input"),
#     "Ethics and Compliance": st.number_input("Ethics and Compliance", min_value=0, value=100, step=10, key="ethics_compliance_input"),
#     "Greenhouse gas emissions (tonnes CO2e)": st.number_input("Greenhouse gas emissions (tonnes CO2e)", min_value=0, value=100, step=10, key="ghg_emissions_input"),
#     "Energy usage (MWh)": st.number_input("Energy usage (MWh)", min_value=0, value=100, step=10, key="energy_usage_input"),
#     "Water usage (cubic meters)": st.number_input("Water usage (cubic meters)", min_value=0, value=100, step=10, key="water_usage_input"),
# }

# # Add new data to DataFrame
# if st.button("Add Data", key="add_data_button"):
#     df_excel = pd.concat([df_excel, pd.DataFrame([new_data])], ignore_index=True)
#     df_excel.to_excel(excel_file, index=False)  # Save updated DataFrame to Excel
#     st.success("Data added successfully!")

# # Input fields for filtering data
# selected_sector = st.selectbox("Select Sector", df_excel["Sector"].unique(), key="sector_filter")
# selected_industry = st.selectbox("Select Industry", df_excel["Industry"].unique(), key="industry_filter")

# # Filter DataFrame based on user inputs
# filtered_df = df_excel[(df_excel["Sector"] == selected_sector) & (df_excel["Industry"] == selected_industry)]

# # Display filtered DataFrame
# st.dataframe(filtered_df)

# # Get the lowest E value of the filtered companies
# lowest_e_value = filtered_df["E"].min()

# # Check if the user's E value is lower than the lowest of the filtered companies
# if new_data["E"] < lowest_e_value:
#     st.warning("The Environmental Score (E) of your input is lower than the lowest E score of the filtered companies.")

#     # Compare the E factors of each company and the user's input
#     comparison_df = filtered_df[required_columns].copy()
#     user_row = pd.Series({
#         "Company": "Your Input",
#         "Greenhouse gas emissions (tonnes CO2e)": new_data["Greenhouse gas emissions (tonnes CO2e)"],
#         "Energy usage (MWh)": new_data["Energy usage (MWh)"],
#         "Water usage (cubic meters)": new_data["Water usage (cubic meters)"]
#     })
#     comparison_df = pd.concat([comparison_df, pd.DataFrame([user_row])], ignore_index=True)

#     # Display comparison DataFrame
#     st.dataframe(comparison_df)

#     # Plot comparison charts
#     fig, axes = plt.subplots(3, 1, figsize=(10, 15))
#     comparison_df.set_index("Company")[["Greenhouse gas emissions (tonnes CO2e)"]].plot(kind="bar", ax=axes[0], color=['blue' if x != 'Your Input' else 'red' for x in comparison_df["Company"]])
#     axes[0].set_title("Greenhouse Gas Emission")
#     comparison_df.set_index("Company")[["Energy usage (MWh)"]].plot(kind="bar", ax=axes[1], color=['blue' if x != 'Your Input' else 'red' for x in comparison_df["Company"]])
#     axes[1].set_title("Energy Usage")
#     comparison_df.set_index("Company")[["Water usage (cubic meters)"]].plot(kind="bar", ax=axes[2], color=['blue' if x != 'Your Input' else 'red' for x in comparison_df["Company"]])
#     axes[2].set_title("Water Usage")
#     st.pyplot(fig)

# # Visualization section
# plot_type = st.selectbox("Select Plot Type", ["Bar Chart", "Line Chart", "Area Chart"], key="plot_type")

# # Select columns to plot
# columns_to_plot = st.multiselect("Select Columns to Plot", df_excel.columns.tolist(), default=["ESG Score"], key="columns_to_plot")

# # Generate plots based on user selection
# if plot_type == "Bar Chart":
#     st.bar_chart(filtered_df[columns_to_plot])
# elif plot_type == "Line Chart":
#     st.line_chart(filtered_df[columns_to_plot])
# elif plot_type == "Area Chart":
#     st.area_chart(filtered_df[columns_to_plot])


# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the Excel file
# excel_file = "ESG.xlsx"
# df_excel = pd.read_excel(excel_file)

# # Required columns for comparison
# required_columns = ["Company", "Greenhouse gas emissions (tonnes CO2e)", "Energy usage (MWh)", "Water usage (cubic meters)"]

# # Ensure the required columns are in the DataFrame
# for col in required_columns:
#     if col not in df_excel.columns:
#         st.error(f"Column '{col}' not found in the Excel file. Please check the file.")
#         st.stop()

# # Streamlit app
# st.title("ESG Data Input and Visualization")

# # Input fields for user to add new data
# new_data = {
#     "Rank": st.number_input("Rank", min_value=1, value=1, step=1, key="rank_input"),
#     "Company": st.text_input("Company", key="company_input"),
#     "Region": st.text_input("Region", key="region_input"),
#     "Country": st.text_input("Country", key="country_input"),
#     "Sector": "",  # Removed from input
#     "Industry": "",  # Removed from input
#     "ESG Score": st.number_input("ESG Score", min_value=0, max_value=100, value=50, step=1, key="esg_score_input"),
#     "Temperature Score (2050)": st.number_input("Temperature Score (2050)", min_value=0.0, max_value=5.0, value=2.0, step=0.1, key="temp_score_input"),
#     "Emissions: Tonnes of CO2e (Scope 1 & 2)": st.number_input("Emissions: Tonnes of CO2e (Scope 1 & 2)", min_value=0, value=1000, step=100, key="emissions_scope1_2_input"),
#     "Emissions: Tonnes of CO2e (Scope 3)": st.number_input("Emissions: Tonnes of CO2e (Scope 3)", min_value=0, value=1000, step=100, key="emissions_scope3_input"),
#     "Market Cap Category": st.text_input("Market Cap Category", key="market_cap_category_input"),
#     "E": st.number_input("E (Environmental Score)", min_value=0, max_value=100, value=20, step=1, key="e_input"),
#     "S": st.number_input("S (Social Score)", min_value=0, max_value=100, value=50, step=1, key="s_input"),
#     "G": st.number_input("G (Governance Score)", min_value=0, max_value=100, value=50, step=1, key="g_input"),
#     "DEI Labor Practices": st.number_input("DEI Labor Practices", min_value=0, value=100, step=10, key="dei_labor_practices_input"),
#     "Community Management": st.number_input("Community Management", min_value=0, value=100, step=10, key="community_management_input"),
#     "Board Diversity": st.number_input("Board Diversity", min_value=0, value=100, step=10, key="board_diversity_input"),
#     "Executive Compensation": st.number_input("Executive Compensation", min_value=0, value=100, step=10, key="executive_compensation_input"),
#     "Ethics and Compliance": st.number_input("Ethics and Compliance", min_value=0, value=100, step=10, key="ethics_compliance_input"),
#     "Greenhouse gas emissions (tonnes CO2e)": st.number_input("Greenhouse gas emissions (tonnes CO2e)", min_value=0, value=100, step=10, key="ghg_emissions_input"),
#     "Energy usage (MWh)": st.number_input("Energy usage (MWh)", min_value=0, value=100, step=10, key="energy_usage_input"),
#     "Water usage (cubic meters)": st.number_input("Water usage (cubic meters)", min_value=0, value=100, step=10, key="water_usage_input"),
# }

# # Add new data to DataFrame
# if st.button("Add Data", key="add_data_button"):
#     df_excel = pd.concat([df_excel, pd.DataFrame([new_data])], ignore_index=True)
#     df_excel.to_excel(excel_file, index=False)  # Save updated DataFrame to Excel
#     st.success("Data added successfully!")

# # Input fields for filtering data
# selected_sector = st.selectbox("Select Sector", df_excel["Sector"].unique(), key="sector_filter")

# # Filter the DataFrame to get industries specific to the selected sector
# industries = df_excel[df_excel["Sector"] == selected_sector]["Industry"].unique()
# selected_industry = st.selectbox("Select Industry", industries, key="industry_filter")

# # Filter DataFrame based on user inputs
# filtered_df = df_excel[(df_excel["Sector"] == selected_sector) & (df_excel["Industry"] == selected_industry)]

# # Display filtered DataFrame
# st.dataframe(filtered_df)

# # Get the lowest E value of the filtered companies
# lowest_e_value = filtered_df["E"].min()

# # Check if the user's E value is lower than the lowest of the filtered companies
# if new_data["E"] < lowest_e_value:
#     st.warning("The Environmental Score (E) of your input is lower than the lowest E score of the filtered companies.")

#     # Compare the E factors of each company and the user's input
#     comparison_df = filtered_df[required_columns].copy()
#     user_row = pd.Series({
#         "Company": "Your Input",
#         "Greenhouse gas emissions (tonnes CO2e)": new_data["Greenhouse gas emissions (tonnes CO2e)"],
#         "Energy usage (MWh)": new_data["Energy usage (MWh)"],
#         "Water usage (cubic meters)": new_data["Water usage (cubic meters)"]
#     })
#     comparison_df = pd.concat([comparison_df, pd.DataFrame([user_row])], ignore_index=True)

#     # Display comparison DataFrame
#     st.dataframe(comparison_df)

#     # Plot comparison charts
#     fig, axes = plt.subplots(3, 1, figsize=(10, 15))
#     comparison_df.set_index("Company")[["Greenhouse gas emissions (tonnes CO2e)"]].plot(kind="bar", ax=axes[0], color=['blue' if x != 'Your Input' else 'red' for x in comparison_df["Company"]])
#     axes[0].set_title("Greenhouse Gas Emission")
#     comparison_df.set_index("Company")[["Energy usage (MWh)"]].plot(kind="bar", ax=axes[1], color=['blue' if x != 'Your Input' else 'red' for x in comparison_df["Company"]])
#     axes[1].set_title("Energy Usage")
#     comparison_df.set_index("Company")[["Water usage (cubic meters)"]].plot(kind="bar", ax=axes[2], color=['blue' if x != 'Your Input' else 'red' for x in comparison_df["Company"]])
#     axes[2].set_title("Water Usage")
#     st.pyplot(fig)

# # Visualization section
# plot_type = st.selectbox("Select Plot Type", ["Bar Chart", "Line Chart", "Area Chart"], key="plot_type")

# # Select columns to plot
# columns_to_plot = st.multiselect("Select Columns to Plot", df_excel.columns.tolist(), default=["ESG Score"], key="columns_to_plot")

# # Generate plots based on user selection
# if plot_type == "Bar Chart":
#     st.bar_chart(filtered_df[columns_to_plot])
# elif plot_type == "Line Chart":
#     st.line_chart(filtered_df[columns_to_plot])
# elif plot_type == "Area Chart":
#     st.area_chart(filtered_df[columns_to_plot])


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
excel_file = "ESG.xlsx"
df_excel = pd.read_excel(excel_file)

# Required columns for comparison
required_columns = ["Company", "Greenhouse gas emissions (tonnes CO2e)", "Energy usage (MWh)", "Water usage (cubic meters)"]

# Ensure the required columns are in the DataFrame
for col in required_columns:
    if col not in df_excel.columns:
        st.error(f"Column '{col}' not found in the Excel file. Please check the file.")
        st.stop()

# Streamlit app
st.title("ESG Data Input and Visualization")

# Input fields for user to add new data
new_data = {
    "Rank": st.number_input("Rank", min_value=1, value=1, step=1, key="rank_input"),
    "Company": st.text_input("Company", key="company_input"),
    "Region": st.text_input("Region", key="region_input"),
    "Country": st.text_input("Country", key="country_input"),
    "Sector": "",  # Removed from input
    "Industry": "",  # Removed from input
    "ESG Score": st.number_input("ESG Score", min_value=0, max_value=100, value=50, step=1, key="esg_score_input"),
    "Temperature Score (2050)": st.number_input("Temperature Score (2050)", min_value=0.0, max_value=5.0, value=2.0, step=0.1, key="temp_score_input"),
    "Emissions: Tonnes of CO2e (Scope 1 & 2)": st.number_input("Emissions: Tonnes of CO2e (Scope 1 & 2)", min_value=0, value=1000, step=100, key="emissions_scope1_2_input"),
    "Emissions: Tonnes of CO2e (Scope 3)": st.number_input("Emissions: Tonnes of CO2e (Scope 3)", min_value=0, value=1000, step=100, key="emissions_scope3_input"),
    "Market Cap Category": st.text_input("Market Cap Category", key="market_cap_category_input"),
    "E": st.number_input("E (Environmental Score)", min_value=0, max_value=100, value=20, step=1, key="e_input"),
    "S": st.number_input("S (Social Score)", min_value=0, max_value=100, value=50, step=1, key="s_input"),
    "G": st.number_input("G (Governance Score)", min_value=0, max_value=100, value=50, step=1, key="g_input"),
    "DEI Labor Practices": st.number_input("DEI Labor Practices", min_value=0, value=100, step=10, key="dei_labor_practices_input"),
    "Community Management": st.number_input("Community Management", min_value=0, value=100, step=10, key="community_management_input"),
    "Board Diversity": st.number_input("Board Diversity", min_value=0, value=100, step=10, key="board_diversity_input"),
    "Executive Compensation": st.number_input("Executive Compensation", min_value=0, value=100, step=10, key="executive_compensation_input"),
    "Ethics and Compliance": st.number_input("Ethics and Compliance", min_value=0, value=100, step=10, key="ethics_compliance_input"),
    "Greenhouse gas emissions (tonnes CO2e)": st.number_input("Greenhouse gas emissions (tonnes CO2e)", min_value=0, value=100, step=10, key="ghg_emissions_input"),
    "Energy usage (MWh)": st.number_input("Energy usage (MWh)", min_value=0, value=100, step=10, key="energy_usage_input"),
    "Water usage (cubic meters)": st.number_input("Water usage (cubic meters)", min_value=0, value=100, step=10, key="water_usage_input"),
}

# Add new data to DataFrame
if st.button("Add Data", key="add_data_button"):
    df_excel = pd.concat([df_excel, pd.DataFrame([new_data])], ignore_index=True)
    df_excel.to_excel(excel_file, index=False)  # Save updated DataFrame to Excel
    st.success("Data added successfully!")

# Input fields for filtering data
selected_sector = st.selectbox("Select Sector", df_excel["Sector"].unique(), key="sector_filter")

# Filter the DataFrame to get industries specific to the selected sector
industries = df_excel[df_excel["Sector"] == selected_sector]["Industry"].unique()
selected_industry = st.selectbox("Select Industry", industries, key="industry_filter")

# Filter DataFrame based on user inputs
filtered_df = df_excel[(df_excel["Sector"] == selected_sector) & (df_excel["Industry"] == selected_industry)]

# Display filtered DataFrame
st.dataframe(filtered_df)

# Get the lowest E, S, and G values of the filtered companies
lowest_e_value = filtered_df["E"].min()
lowest_s_value = filtered_df["S"].min()
lowest_g_value = filtered_df["G"].min()

# Check if the user's E, S, or G value is lower than the lowest of the filtered companies
if new_data["E"] < lowest_e_value:
    st.warning("The Environmental Score (E) of your input is lower than the lowest E score of the filtered companies.")

    # Compare the E factors of each company and the user's input
    comparison_df_e = filtered_df[required_columns].copy()
    user_row_e = pd.Series({
        "Company": "Input",
        "Greenhouse gas emissions (tonnes CO2e)": new_data["Greenhouse gas emissions (tonnes CO2e)"],
        "Energy usage (MWh)": new_data["Energy usage (MWh)"],
        "Water usage (cubic meters)": new_data["Water usage (cubic meters)"]
    })
    comparison_df_e = pd.concat([comparison_df_e, pd.DataFrame([user_row_e])], ignore_index=True)

    # Display comparison DataFrame for E
    st.dataframe(comparison_df_e)

    # Plot comparison charts for E
    fig, axes = plt.subplots(3, 1, figsize=(10, 15))
    comparison_df_e.set_index("Company")[["Greenhouse gas emissions (tonnes CO2e)"]].plot(kind="bar", ax=axes[0], color=['blue' if x != 'Your Input' else 'red' for x in comparison_df_e["Company"]])
    axes[0].set_title("Greenhouse Gas Emission")
    fig.subplots_adjust(wspace=1,hspace=1.0)
    comparison_df_e.set_index("Company")[["Energy usage (MWh)"]].plot(kind="bar", ax=axes[1], color=['blue' if x != 'Your Input' else 'red' for x in comparison_df_e["Company"]])
    axes[1].set_title("Energy Usage")
    fig.subplots_adjust(wspace=1,hspace=1.0)
    comparison_df_e.set_index("Company")[["Water usage (cubic meters)"]].plot(kind="bar", ax=axes[2], color=['blue' if x != 'Your Input' else 'red' for x in comparison_df_e["Company"]])
    axes[2].set_title("Water Usage")
    fig.subplots_adjust(wspace=1,hspace=1.0)
    st.pyplot(fig)

if new_data["S"] < lowest_s_value:
    st.warning("The Social Score (S) of your input is lower than the lowest S score of the filtered companies.")

    # Compare the S factors of each company and the user's input
    comparison_df_s = filtered_df[required_columns].copy()
    user_row_s = pd.Series({
        "Company": "Input",
        "Greenhouse gas emissions (tonnes CO2e)": new_data["Greenhouse gas emissions (tonnes CO2e)"],
        "Energy usage (MWh)": new_data["Energy usage (MWh)"],
        "Water usage (cubic meters)": new_data["Water usage (cubic meters)"]
    })
    comparison_df_s = pd.concat([comparison_df_s, pd.DataFrame([user_row_s])], ignore_index=True)

    # Display comparison DataFrame for S
    st.dataframe(comparison_df_s)

    # Plot comparison charts for S
    fig, axes = plt.subplots(3, 1, figsize=(10, 15))
    comparison_df_s.set_index("Company")[["Greenhouse gas emissions (tonnes CO2e)"]].plot(kind="bar", ax=axes[0], color=['blue' if x != 'Your Input' else 'red' for x in comparison_df_s["Company"]])
    axes[0].set_title("Greenhouse Gas Emission")
    fig.subplots_adjust(wspace=1,hspace=1.0)
    comparison_df_s.set_index("Company")[["Energy usage (MWh)"]].plot(kind="bar", ax=axes[1], color=['blue' if x != 'Your Input' else 'red' for x in comparison_df_s["Company"]])
    axes[1].set_title("Energy Usage")
    fig.subplots_adjust(wspace=1,hspace=1.0)
    comparison_df_s.set_index("Company")[["Water usage (cubic meters)"]].plot(kind="bar", ax=axes[2], color=['blue' if x != 'Your Input' else 'red' for x in comparison_df_s["Company"]])
    axes[2].set_title("Water Usage")
    fig.subplots_adjust(wspace=1,hspace=1.0)
    st.pyplot(fig)

if new_data["G"] < lowest_g_value:
    st.warning("The Governance Score (G) of your input is lower than the lowest G score of the filtered companies.")

    # Compare the G factors of each company and the user's input
    comparison_df_g = filtered_df[required_columns].copy()
    user_row_g = pd.Series({
        "Company": "Input",
        "Greenhouse gas emissions (tonnes CO2e)": new_data["Greenhouse gas emissions (tonnes CO2e)"],
        "Energy usage (MWh)": new_data["Energy usage (MWh)"],
        "Water usage (cubic meters)": new_data["Water usage (cubic meters)"]
    })
    comparison_df_g = pd.concat([comparison_df_g, pd.DataFrame([user_row_g])], ignore_index=True)

    # Display comparison DataFrame for G
    st.dataframe(comparison_df_g)

    # Plot comparison charts for G
    fig, axes = plt.subplots(3, 1, figsize=(10, 15))
    comparison_df_g.set_index("Company")[["Greenhouse gas emissions (tonnes CO2e)"]].plot(kind="bar", ax=axes[0], color=['blue' if x != 'Your Input' else 'red' for x in comparison_df_g["Company"]])
    axes[0].set_title("Greenhouse Gas Emission")
    fig.subplots_adjust(wspace=1,hspace=1.0)
    comparison_df_g.set_index("Company")[["Energy usage (MWh)"]].plot(kind="bar", ax=axes[1], color=['blue' if x != 'Your Input' else 'red' for x in comparison_df_g["Company"]])
    axes[1].set_title("")
    fig.subplots_adjust(wspace=1,hspace=1.0)
    comparison_df_g.set_index("Company")[["Water usage (cubic meters)"]].plot(kind="bar", ax=axes[2], color=['blue' if x != 'Your Input' else 'red' for x in comparison_df_g["Company"]])
    axes[2].set_title("")
    fig.subplots_adjust(wspace=1,hspace=1.0)
    st.pyplot(fig)

# Visualization section
plot_type = st.selectbox("Select Plot Type", ["Bar Chart", "Line Chart", "Area Chart"], key="plot_type")

# Select columns to plot
columns_to_plot = st.multiselect("Select Columns to Plot", df_excel.columns.tolist(), default=["ESG Score"], key="columns_to_plot")

# Generate plots based on user selection
if plot_type == "Bar Chart":
    st.bar_chart(filtered_df[columns_to_plot])
elif plot_type == "Line Chart":
    st.line_chart(filtered_df[columns_to_plot])
elif plot_type == "Area Chart":
    st.area_chart(filtered_df[columns_to_plot])

