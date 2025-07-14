# Geospatial Point Aggregation Using H3

This Python script aggregates geolocated point data into approximately 1 km² hexagonal zones using the H3 geospatial indexing system. It is useful for spatial clustering, density analysis, and visualizing concentrations of point-based geodata.

---

## ✅ Features

- Reads geospatial point data from an Excel file  
- Cleans and validates latitude/longitude input  
- Assigns each coordinate to an H3 cell (resolution 8 ≈ 1 km²)  
- Counts how many points fall within each hex cell  
- Computes the centroid of each H3 cell  
- Saves the result to a new Excel file  

---

## 📦 Requirements

To run the script, install the following Python packages:

```bash
pip install pandas h3 openpyxl
````

---

## 🚀 Usage

1. Clone or download this repository.
2. Run the script in a terminal or IDE:

```bash
python h3_density_mapper.py
```

3. You will be prompted to:

   * Enter the path to your input Excel file
   * Provide the desired output path for the results

---

## 📄 Input Format

Your Excel file should include the following columns:

* `latitude`
* `longitude`

These can be in any order. Column names are case-insensitive, and leading/trailing spaces will be trimmed.

---

## 🗂 Output

The output Excel file will contain:

* `h3_cell`: the H3 hexagon ID (resolution 8)
* `count`: the number of points in that hexagon
* `centroid_lat`: latitude of the hexagon center
* `centroid_lng`: longitude of the hexagon center

---

## 🧭 Customization

You can change the H3 resolution (currently set to 8) in the script to adjust the size of the aggregation cells.

📘 Refer to the [H3 Resolution Guide](https://h3geo.org/docs/core-library/restable/) for more details on hexagon sizes.

---

## 📃 License

This project is released under the MIT License.
