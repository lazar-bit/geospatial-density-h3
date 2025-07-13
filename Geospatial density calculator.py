import pandas as pd
import h3
import os

# ✅ Ask user for input and output file paths instead of hardcoding
input_path = input("Enter the path to the input Excel file: ").strip()
output_path = input("Enter the desired path for the output Excel file: ").strip()

# ✅ Load Excel file
df = pd.read_excel(input_path)

# ✅ Clean column names to remove leading/trailing spaces
df.columns = df.columns.str.strip()

# ✅ Convert coordinates to numeric, force invalid entries to NaN
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')

# ✅ Drop rows with missing coordinates
df = df.dropna(subset=['latitude', 'longitude'])

# ✅ Use H3 to assign 1 km² hexagonal cells (resolution 8)
df['h3_cell'] = df.apply(lambda row: h3.latlng_to_cell(row['latitude'], row['longitude'], 8), axis=1)

# ✅ Count how many losses fall into each H3 cell
counts = df['h3_cell'].value_counts().reset_index()
counts.columns = ['h3_cell', 'loss_count']

# ✅ Add centroids (lat/lng) for each H3 cell
counts['centroid_lat'] = counts['h3_cell'].apply(lambda cell: h3.cell_to_latlng(cell)[0])
counts['centroid_lng'] = counts['h3_cell'].apply(lambda cell: h3.cell_to_latlng(cell)[1])

# ✅ Save results to Excel
counts.to_excel(output_path, index=False)

# ✅ Output summary
print("\n✅ Done. Top 10 densest 1 km² zones:")
print(counts.head(10))
