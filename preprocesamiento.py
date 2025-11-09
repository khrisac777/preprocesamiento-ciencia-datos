import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocesamiento_completo(df):
    print("Iniciando preprocesamiento...")
    print(f"Dataset original con {df.shape[0]} filas y {df.shape[1]} columnas.")

    df = df.drop_duplicates()
    print(f"Después de eliminar duplicados: {df.shape[0]} filas.")

    numeric_cols = df.select_dtypes(include=['number']).columns
    categoric_cols = df.select_dtypes(include=['object', 'category']).columns

    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].mean())
        
    for col in categoric_cols:
        df[col] = df[col].fillna(df[col].mode()[0])
    
    print("Valores nulos gestionados.")

    if not categoric_cols.empty:
        df = pd.get_dummies(df, columns=categoric_cols, drop_first=True)
        print("Variables categóricas codificadas.")
    
    scaler = MinMaxScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    print("Variables numéricas normalizadas.")
    
    print("¡Preprocesamiento completado!")
    return df

if __name__ == "__main__":
    # Ejemplo de uso con un dataset de prueba
    data = {
        'Edad': [25, 30, 30, 45, 25, None, 50],
        'Ciudad': ['NY', 'SF', 'SF', 'NY', 'Chicago', 'SF', 'NY'],
        'Ingresos': [50000, 80000, 80000, 120000, 45000, 75000, None],
        'Compra': ['No', 'Si', 'Si', 'Si', 'No', 'Si', 'No']
    }
    df_prueba = pd.DataFrame(data)
    
    print("--- Dataset Original ---")
    print(df_prueba)
    
    df_procesado = preprocesamiento_completo(df_prueba)
    
    print("\n--- Dataset Procesado ---")
    print(df_procesado)