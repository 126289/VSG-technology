import numpy as np

def predict_with_models(sample, models):
    """
    Predict the sample's output using each of the K models.
    
    :param sample: The new online sample.
    :param models: A list of K trained models.
    :return: A list of predictions from each model.
    """
    predictions = [model.predict(sample) for model in models]
    return predictions

def compute_bayesian_weights(sample, predictions):
    """
    Compute the Bayesian weights for each mode based on the sample and model predictions.
    
    :param sample: The new online sample.
    :param predictions: Predictions from each of the K models.
    :return: A list of weights for each prediction.
    """
    # Placeholder for the actual computation of Bayesian weights
    # This should be replaced with actual Bayesian inference computation
    weights = [1/len(predictions)] * len(predictions)  # Equal weights as a placeholder
    return weights

def weighted_average(predictions, weights):
    """
    Compute the weighted average of predictions.
    
    :param predictions: Predictions from each of the K models.
    :param weights: Computed weights for each prediction.
    :return: Weighted average of the predictions.
    """
    weighted_sum = sum(p * w for p, w in zip(predictions, weights))
    return weighted_sum

# Example usage
sample = np.array([0.5, 0.2])  # An example online sample
models = [model1, model2, model3]  # Your K models should be defined or loaded here

predictions = predict_with_models(sample.reshape(1, -1), models)  # Ensure sample is the correct shape
weights = compute_bayesian_weights(sample, predictions)
weighted_pred = weighted_average(predictions, weights)

print(f"Weighted prediction: {weighted_pred}")
