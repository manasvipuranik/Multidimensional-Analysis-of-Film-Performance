import pandas as pd
import re
import os

# === CONFIG ===
INPUT_FILE = r"C:\Users\MANASVI\Desktop\SSIS\Movies Dataset\netflix_titles.csv"
OUTPUT_FILE = r"C:\Users\MANASVI\Desktop\SSIS\Movies Dataset\cleaned_netflix.csv"
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

# === 1️⃣ EXTRACT ===
print("📥 Loading dataset...")
df = pd.read_csv(INPUT_FILE, encoding="utf-8")
print(f"✅ Loaded! Shape: {df.shape}")

# === 2️⃣ CLEAN FUNCTION ===
def clean_text(text):
    """Remove commas, special chars, and extra spaces from text fields."""
    if pd.isna(text):
        return ""
    text = str(text).lower()                     # lowercase
    text = text.replace(",", " ")                # replace commas with spaces
    text = re.sub(r"[^\w\s]", " ", text)         # remove special characters
    text = re.sub(r"\s+", " ", text)             # collapse multiple spaces
    return text.strip()

# Apply cleaning to all object columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].apply(clean_text)

# === 3️⃣ DROP DUPLICATES & EMPTY ROWS ===
df.drop_duplicates(inplace=True)
df.dropna(how="all", inplace=True)

# === 4️⃣ SAVE CLEANED CSV ===
df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

print("✅ Cleaning complete!")
print(f"📁 Cleaned file saved to: {OUTPUT_FILE}")
print(f"📊 Final shape: {df.shape}")
