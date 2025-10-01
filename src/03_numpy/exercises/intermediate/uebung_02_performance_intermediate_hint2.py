#!/usr/bin/env python3
"""
🟡 INTERMEDIATE - NumPy Performance-Optimierung - HINT 2 (Konkrete Ansätze)
Übung 2: Performance-Optimierung für SmartFactory Datenverarbeitung

🎯 KONKRETE STRATEGIEN mit Pseudo-Code:
"""


def konkrete_loesungsansaetze():
    """Konkrete Lösungsansätze mit Pseudo-Code"""
    print("=" * 60)
    print("🟡 HINT 2: Konkrete Performance-Strategien")
    print("=" * 60)

    print("🔧 VECTORIZATION-STRATEGIEN:")
    print(
        """
# Pseudo-Code:
# Schlecht: Python-Loop
result = []
for i in range(len(data)):
    result.append(math.sqrt(data[i] ** 2 + offset))

# Besser: NumPy vectorized
result = np.sqrt(data ** 2 + offset)

# Noch besser: In-place für große Arrays
data **= 2
data += offset
np.sqrt(data, out=data)  # In-place sqrt
"""
    )

    print("🔧 MEMORY-LAYOUT-OPTIMIERUNG:")
    print(
        """
# Pseudo-Code:
# Cache-freundlich: Row-wise access
for row in range(matrix.shape[0]):
    row_sum = np.sum(matrix[row, :])  # Zusammenhängender Speicher

# Cache-unfreundlich: Column-wise bei C-layout
for col in range(matrix.shape[1]):
    col_sum = np.sum(matrix[:, col])  # Scattered Memory Access

# Optimiert: Transpose für Column-Operations
matrix_T = matrix.T  # Einmaliger Overhead
for col in range(matrix_T.shape[0]):  # Jetzt row-wise
    col_sum = np.sum(matrix_T[col, :])
"""
    )

    print("🔧 BATCH-PROCESSING:")
    print(
        """
# Pseudo-Code:
# Ineffizient: Element-weise
results = []
for item in large_dataset:
    processed = expensive_function(item)
    results.append(processed)

# Effizient: Batch-weise
batch_size = 1000
for i in range(0, len(large_dataset), batch_size):
    batch = large_dataset[i:i+batch_size]
    batch_results = expensive_function_vectorized(batch)
    results.extend(batch_results)
"""
    )

    print("🔧 PRE-ALLOCATION:")
    print(
        """
# Pseudo-Code:
# Schlecht: Dynamic growth
results = []
for i in range(n):
    results.append(compute_value(i))

# Besser: Pre-allocated
results = np.empty(n, dtype=np.float64)
for i in range(n):
    results[i] = compute_value(i)

# Optimal: Vectorized
results = compute_value_vectorized(np.arange(n))
"""
    )


if __name__ == "__main__":
    konkrete_loesungsansaetze()
