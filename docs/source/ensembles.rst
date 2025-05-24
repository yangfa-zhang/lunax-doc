lunax.ensembles
=====================

This module implements a hill climbing algorithm for optimizing ensemble model weights.

.. py:class:: HillClimbingEnsemble

   A class that implements hill climbing optimization for ensemble model weights.

   :param models: List of trained model instances inheriting from BaseModel
   :type models: List[BaseModel]
   :param metric: Evaluation metric(s) to optimize ('accuracy', 'precision', 'recall', 'f1', 'auc')
   :type metric: Union[str, List[str]]
   :param maximize: Whether to maximize the metric (True) or minimize it (False)
   :type maximize: bool
   :param max_iter: Maximum number of iterations for each random start
   :type max_iter: int
   :param step_size: Step size for weight adjustments
   :type step_size: float
   :param tolerance: Convergence threshold
   :type tolerance: float
   :param n_random_starts: Number of random initializations
   :type n_random_starts: int
   :param random_state: Random seed for reproducibility
   :type random_state: Optional[int]

   **Methods:**

   .. py:method:: fit(X_val: pd.DataFrame, y_val: pd.Series) -> np.ndarray

      Optimize ensemble weights using hill climbing.

      :param X_val: Validation features
      :param y_val: Validation labels
      :return: Optimal weights array
      :rtype: np.ndarray

   .. py:method:: predict(X: pd.DataFrame) -> np.ndarray

      Make predictions using the optimized ensemble.

      :param X: Input features
      :return: Predicted labels
      :rtype: np.ndarray
      :raises ValueError: If model hasn't been fitted

   .. py:method:: predict_proba(X: pd.DataFrame) -> np.ndarray

      Get probability predictions using the optimized ensemble.

      :param X: Input features
      :return: Predicted probabilities
      :rtype: np.ndarray
      :raises ValueError: If model hasn't been fitted

   **Private Methods:**

   .. py:method:: _get_ensemble_predictions(X: pd.DataFrame, weights: np.ndarray) -> tuple[np.ndarray, np.ndarray]

      Get weighted ensemble predictions.

      :return: Tuple of (probabilities, labels)

   .. py:method:: _evaluate_weights(weights: np.ndarray, X: pd.DataFrame, y: pd.Series) -> float

      Evaluate current weight combination performance.

      :return: Evaluation score

   .. py:method:: _get_neighbors(weights: np.ndarray) -> List[np.ndarray]

      Get neighboring weight combinations.

      :return: List of neighbor weight arrays

   **Features:**

   - Supports multiple evaluation metrics
   - Handles both binary and multi-class classification
   - Implements weighted averaging of model predictions
   - Maintains optimization history
   - Ensures weights sum to 1 and are non-negative

   **Example Usage:**

   .. code-block:: python

      from lunax.ensembles import HillClimbingEnsemble

      # Initialize with trained models
      ensemble = HillClimbingEnsemble(
          models=[model1, model2, model3],
          metric=['accuracy', 'f1'],
          max_iter=100,
          n_random_starts=5
      )

      # Optimize weights
      best_weights = ensemble.fit(X_val, y_val)

      # Make predictions
      predictions = ensemble.predict(X_test)
      probabilities = ensemble.predict_proba(X_test)

   **Notes:**

   - The algorithm performs multiple random starts to avoid local optima
   - Convergence is determined by the tolerance parameter
   - Supports both single and multiple metric optimization
   - Automatically handles probability and non-probability predictions
   - Implements weighted model averaging for ensemble predictions