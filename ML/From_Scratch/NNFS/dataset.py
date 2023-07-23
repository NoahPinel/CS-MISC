import numpy as np
def dataset_gen(num_points_per_class):
    # Random seed for reproducibility
    np.random.seed(0)
    num_classes = 5
    data = []
    labels = []

    for class_index in range(num_classes):
        # Generate random points with some variance
        X = np.random.randn(num_points_per_class, 2) + class_index * 3

        data.append(X)

        y = np.ones(num_points_per_class, dtype=np.int32) * class_index  # Convert to integer type
        labels.append(y)

    X = np.concatenate(data)
    y = np.concatenate(labels)
    
    indices = np.arange(X.shape[0])
    np.random.shuffle(indices)
    
    X = X[indices]
    y = y[indices]
    return X, y
