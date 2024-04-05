import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
num_samples = 1000

# Features
THC_content = np.random.uniform(0, 30, num_samples)
CBD_content = np.random.uniform(0, 30, num_samples)
terpene_profile = np.random.uniform(0, 1, (num_samples, 5))  # Assuming 5 different terpenes

# Target variable
effectiveness = np.random.randint(0, 2, num_samples)  # Binary variable indicating effectiveness (0 or 1)

# Create DataFrame
data = pd.DataFrame({
    'THC_content': THC_content,
    'CBD_content': CBD_content,
    'Terpene_1': terpene_profile[:, 0],
    'Terpene_2': terpene_profile[:, 1],
    'Terpene_3': terpene_profile[:, 2],
    'Terpene_4': terpene_profile[:, 3],
    'Terpene_5': terpene_profile[:, 4],
    'Effectiveness': effectiveness
})

# Save DataFrame to CSV
data.to_csv('cannabis_data.csv', index=False)
