lunax.data_processing
========================

This module provides utility functions for data loading, splitting, and preprocessing operations.

.. py:function:: load_data(file_path: str) -> pd.DataFrame

   Load tabular data from a file into a DataFrame.

   :param file_path: Path to the data file (supports csv, parquet, xlsx, xls)
   :type file_path: str
   :return: Loaded data as DataFrame
   :rtype: pd.DataFrame
   :raises ValueError: If file format is not supported
   :raises Exception: If data loading fails

.. py:function:: split_data(df: pd.DataFrame, target: str, test_size: float = 0.2, random_state: int = 42) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]

   Split dataset into training and validation sets.

   :param df: Input DataFrame
   :type df: pd.DataFrame
   :param target: Name of the target column
   :type target: str
   :param test_size: Proportion of the dataset to include in the validation split
   :type test_size: float
   :param random_state: Random seed for reproducibility
   :type random_state: int
   :return: X_train, X_val, y_train, y_val
   :rtype: Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]

.. py:function:: preprocess_data(df: pd.DataFrame, target: str = None, numeric_strategy: str = "mean", category_strategy: str = "most_frequent", scale_numeric: bool = True, encode_categorical: bool = True) -> pd.DataFrame

   Perform data preprocessing including missing value handling, encoding, and standardization.

   :param df: Input DataFrame
   :type df: pd.DataFrame
   :param target: Target column name (if any)
   :type target: str, optional
   :param numeric_strategy: Strategy for filling numeric missing values ('mean' or 'median')
   :type numeric_strategy: str
   :param category_strategy: Strategy for filling categorical missing values ('most_frequent')
   :type category_strategy: str
   :param scale_numeric: Whether to standardize numeric features
   :type scale_numeric: bool
   :param encode_categorical: Whether to encode categorical features
   :type encode_categorical: bool
   :return: Preprocessed DataFrame
   :rtype: pd.DataFrame

   **Features:**

   - Handles both numeric and categorical features
   - Supports missing value imputation
   - Performs feature scaling (standardization)
   - Provides label encoding for categorical variables
   - Preserves original data by working on a copy

   **Example Usage:**

   .. code-block:: python

      from lunax.data_processing.utils import preprocess_data

      # Load your data
      df = pd.DataFrame(...)

      # Preprocess with default settings
      processed_df = preprocess_data(df, target='target_column')

      # Customize preprocessing
      processed_df = preprocess_data(
          df,
          target='target_column',
          numeric_strategy='median',
          scale_numeric=False,
          encode_categorical=True
      )