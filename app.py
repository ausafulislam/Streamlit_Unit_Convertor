import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="UniConvert Pro",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to make the app more attractive
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: #f5f7f9;
        }}
        .main-header {{
            font-family: 'Helvetica Neue', sans-serif;
            font-size: 42px;
            font-weight: 700;
            color: #1E3A8A;
            text-align: center;
            margin-bottom: 20px;
            padding-top: 20px;
        }}
        .sub-header {{
            font-family: 'Helvetica Neue', sans-serif;
            font-size: 24px;
            font-weight: 500;
            color: #3B82F6;
            margin-bottom: 10px;
        }}
        .category-card {{
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }}
        .stSelectbox label, .stNumberInput label {{
            font-weight: 500;
            color: #4B5563;
        }}
        .result-card {{
            background-color: #EFF6FF;
            border-radius: 10px;
            padding: 15px;
            margin-top: 10px;
            border-left: 5px solid #3B82F6;
        }}
        .footer {{
            text-align: center;
            margin-top: 30px;
            font-size: 14px;
            color: #6B7280;
        }}
        .stButton button {{
            background-color: #3B82F6;
            color: white;
            font-weight: 500;
            border-radius: 5px;
        }}
        .stButton button:hover {{
            background-color: #2563EB;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()

# App title and description
st.markdown("<h1 class='main-header'>UniConvert Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; margin-bottom: 30px;'>Your ultimate unit conversion companion</p>", unsafe_allow_html=True)

# Create tabs for different conversion categories
tabs = st.tabs(["Length", "Weight", "Temperature", "Area", "Volume", "Speed", "Time"])

# Length conversion
with tabs[0]:
    st.markdown("<div class='category-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Length Conversion</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Enter value", value=1.0, step=0.1, key="length_input")
        from_unit = st.selectbox(
            "From",
            ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
            key="length_from"
        )
    
    with col2:
        to_unit = st.selectbox(
            "To",
            ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
            key="length_to"
        )
        
        # Conversion factors to meter (base unit)
        length_factors = {
            "Meter": 1,
            "Kilometer": 1000,
            "Centimeter": 0.01,
            "Millimeter": 0.001,
            "Mile": 1609.34,
            "Yard": 0.9144,
            "Foot": 0.3048,
            "Inch": 0.0254
        }
        
        # Convert to base unit (meter) then to target unit
        base_value = input_value * length_factors[from_unit]
        result = base_value / length_factors[to_unit]
        
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; margin-bottom: 10px;'>{input_value} {from_unit} = </h3>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center; color: #1E3A8A;'>{result:.6g} {to_unit}</h2>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Weight conversion
with tabs[1]:
    st.markdown("<div class='category-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Weight Conversion</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Enter value", value=1.0, step=0.1, key="weight_input")
        from_unit = st.selectbox(
            "From",
            ["Kilogram", "Gram", "Milligram", "Metric Ton", "Pound", "Ounce", "Stone"],
            key="weight_from"
        )
    
    with col2:
        to_unit = st.selectbox(
            "To",
            ["Kilogram", "Gram", "Milligram", "Metric Ton", "Pound", "Ounce", "Stone"],
            key="weight_to"
        )
        
        # Conversion factors to kilogram (base unit)
        weight_factors = {
            "Kilogram": 1,
            "Gram": 0.001,
            "Milligram": 0.000001,
            "Metric Ton": 1000,
            "Pound": 0.453592,
            "Ounce": 0.0283495,
            "Stone": 6.35029
        }
        
        # Convert to base unit (kilogram) then to target unit
        base_value = input_value * weight_factors[from_unit]
        result = base_value / weight_factors[to_unit]
        
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; margin-bottom: 10px;'>{input_value} {from_unit} = </h3>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center; color: #1E3A8A;'>{result:.6g} {to_unit}</h2>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Temperature conversion
with tabs[2]:
    st.markdown("<div class='category-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Temperature Conversion</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Enter value", value=0.0, step=0.1, key="temp_input")
        from_unit = st.selectbox(
            "From",
            ["Celsius", "Fahrenheit", "Kelvin"],
            key="temp_from"
        )
    
    with col2:
        to_unit = st.selectbox(
            "To",
            ["Celsius", "Fahrenheit", "Kelvin"],
            key="temp_to"
        )
        
        # Temperature conversion requires special formulas
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (input_value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = input_value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (input_value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = ((input_value - 32) * 5/9) + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = input_value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = ((input_value - 273.15) * 9/5) + 32
        else:
            result = input_value  # Same unit
        
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; margin-bottom: 10px;'>{input_value} {from_unit} = </h3>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center; color: #1E3A8A;'>{result:.6g} {to_unit}</h2>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Area conversion
with tabs[3]:
    st.markdown("<div class='category-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Area Conversion</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Enter value", value=1.0, step=0.1, key="area_input")
        from_unit = st.selectbox(
            "From",
            ["Square Meter", "Square Kilometer", "Square Centimeter", "Square Millimeter", 
             "Square Mile", "Square Yard", "Square Foot", "Square Inch", "Hectare", "Acre"],
            key="area_from"
        )
    
    with col2:
        to_unit = st.selectbox(
            "To",
            ["Square Meter", "Square Kilometer", "Square Centimeter", "Square Millimeter", 
             "Square Mile", "Square Yard", "Square Foot", "Square Inch", "Hectare", "Acre"],
            key="area_to"
        )
        
        # Conversion factors to square meter (base unit)
        area_factors = {
            "Square Meter": 1,
            "Square Kilometer": 1000000,
            "Square Centimeter": 0.0001,
            "Square Millimeter": 0.000001,
            "Square Mile": 2589988.11,
            "Square Yard": 0.836127,
            "Square Foot": 0.092903,
            "Square Inch": 0.00064516,
            "Hectare": 10000,
            "Acre": 4046.86
        }
        
        # Convert to base unit (square meter) then to target unit
        base_value = input_value * area_factors[from_unit]
        result = base_value / area_factors[to_unit]
        
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; margin-bottom: 10px;'>{input_value} {from_unit} = </h3>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center; color: #1E3A8A;'>{result:.6g} {to_unit}</h2>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Volume conversion
with tabs[4]:
    st.markdown("<div class='category-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Volume Conversion</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Enter value", value=1.0, step=0.1, key="volume_input")
        from_unit = st.selectbox(
            "From",
            ["Cubic Meter", "Cubic Kilometer", "Cubic Centimeter", "Cubic Millimeter", 
             "Liter", "Milliliter", "US Gallon", "US Quart", "US Pint", "US Cup", 
             "US Fluid Ounce", "US Tablespoon", "US Teaspoon", "Imperial Gallon"],
            key="volume_from"
        )
    
    with col2:
        to_unit = st.selectbox(
            "To",
            ["Cubic Meter", "Cubic Kilometer", "Cubic Centimeter", "Cubic Millimeter", 
             "Liter", "Milliliter", "US Gallon", "US Quart", "US Pint", "US Cup", 
             "US Fluid Ounce", "US Tablespoon", "US Teaspoon", "Imperial Gallon"],
            key="volume_to"
        )
        
        # Conversion factors to cubic meter (base unit)
        volume_factors = {
            "Cubic Meter": 1,
            "Cubic Kilometer": 1000000000,
            "Cubic Centimeter": 0.000001,
            "Cubic Millimeter": 1e-9,
            "Liter": 0.001,
            "Milliliter": 0.000001,
            "US Gallon": 0.00378541,
            "US Quart": 0.000946353,
            "US Pint": 0.000473176,
            "US Cup": 0.000236588,
            "US Fluid Ounce": 2.9574e-5,
            "US Tablespoon": 1.4787e-5,
            "US Teaspoon": 4.9289e-6,
            "Imperial Gallon": 0.00454609
        }
        
        # Convert to base unit (cubic meter) then to target unit
        base_value = input_value * volume_factors[from_unit]
        result = base_value / volume_factors[to_unit]
        
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; margin-bottom: 10px;'>{input_value} {from_unit} = </h3>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center; color: #1E3A8A;'>{result:.6g} {to_unit}</h2>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Speed conversion
with tabs[5]:
    st.markdown("<div class='category-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Speed Conversion</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Enter value", value=1.0, step=0.1, key="speed_input")
        from_unit = st.selectbox(
            "From",
            ["Meter per second", "Kilometer per hour", "Mile per hour", "Foot per second", "Knot"],
            key="speed_from"
        )
    
    with col2:
        to_unit = st.selectbox(
            "To",
            ["Meter per second", "Kilometer per hour", "Mile per hour", "Foot per second", "Knot"],
            key="speed_to"
        )
        
        # Conversion factors to meter per second (base unit)
        speed_factors = {
            "Meter per second": 1,
            "Kilometer per hour": 0.277778,
            "Mile per hour": 0.44704,
            "Foot per second": 0.3048,
            "Knot": 0.514444
        }
        
        # Convert to base unit (meter per second) then to target unit
        base_value = input_value / speed_factors[from_unit]
        result = base_value * speed_factors[to_unit]
        
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; margin-bottom: 10px;'>{input_value} {from_unit} = </h3>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center; color: #1E3A8A;'>{result:.6g} {to_unit}</h2>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Time conversion
with tabs[6]:
    st.markdown("<div class='category-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Time Conversion</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Enter value", value=1.0, step=0.1, key="time_input")
        from_unit = st.selectbox(
            "From",
            ["Second", "Millisecond", "Microsecond", "Nanosecond", "Minute", "Hour", "Day", "Week", "Month (30 days)", "Year (365 days)"],
            key="time_from"
        )
    
    with col2:
        to_unit = st.selectbox(
            "To",
            ["Second", "Millisecond", "Microsecond", "Nanosecond", "Minute", "Hour", "Day", "Week", "Month (30 days)", "Year (365 days)"],
            key="time_to"
        )
        
        # Conversion factors to second (base unit)
        time_factors = {
            "Second": 1,
            "Millisecond": 0.001,
            "Microsecond": 0.000001,
            "Nanosecond": 1e-9,
            "Minute": 60,
            "Hour": 3600,
            "Day": 86400,
            "Week": 604800,
            "Month (30 days)": 2592000,
            "Year (365 days)": 31536000
        }
        
        # Convert to base unit (second) then to target unit
        base_value = input_value * time_factors[from_unit]
        result = base_value / time_factors[to_unit]
        
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; margin-bottom: 10px;'>{input_value} {from_unit} = </h3>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center; color: #1E3A8A;'>{result:.6g} {to_unit}</h2>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Add a footer
st.markdown("<div class='footer'>", unsafe_allow_html=True)
st.markdown("UniConvert Pro - Your Ultimate Unit Conversion Tool", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Add a sidebar with additional information
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>About UniConvert Pro</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);'>
    <p>UniConvert Pro is a powerful unit conversion tool that allows you to convert between various units of measurement with ease.</p>
    <p>Features:</p>
    <ul>
        <li>Convert between multiple unit categories</li>
        <li>Real-time conversion as you type</li>
        <li>Clean and intuitive interface</li>
        <li>Accurate conversion results</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Add a "How to use" section
    st.markdown("<h3 style='color: #3B82F6;'>How to Use</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);'>
    <ol>
        <li>Select a conversion category from the tabs</li>
        <li>Enter the value you want to convert</li>
        <li>Select the source unit from the "From" dropdown</li>
        <li>Select the target unit from the "To" dropdown</li>
        <li>View the conversion result instantly</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

# Display a sample conversion chart for common units
if st.checkbox("Show Common Conversion Chart", value=False):
    st.markdown("<h3 style='color: #3B82F6; margin-top: 20px;'>Common Conversion Chart</h3>", unsafe_allow_html=True)
    
    # Create sample data for the chart
    length_data = {
        'From': ['1 Meter', '1 Kilometer', '1 Inch', '1 Foot', '1 Mile'],
        'To Meters': ['1', '1000', '0.0254', '0.3048', '1609.34'],
        'To Feet': ['3.28084', '3280.84', '0.0833333', '1', '5280'],
        'To Inches': ['39.3701', '39370.1', '1', '12', '63360']
    }
    
    # Display the chart
    st.markdown("<div style='background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);'>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(length_data), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Add a footer
st.markdown("<div class='footer'>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("🔹 **Built with ❤️ by Ausaf Ul Islam** | Stay informed, stay inspired!")
st.markdown("</div>", unsafe_allow_html=True)
