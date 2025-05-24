lunax.viz
==============================

This module provides visualization functions for exploratory data analysis, supporting both numeric and categorical features.

Functions
---------

.. py:function:: numeric_eda(df_list: List[pd.DataFrame], label_list: List[str], target: str, custom_palette: Optional[List[str]] = None) -> None

   Visualize the distribution of numeric features across different datasets.

   :param df_list: List of DataFrames to analyze
   :type df_list: List[pd.DataFrame]
   :param label_list: List of labels for each DataFrame
   :type label_list: List[str]
   :param target: Name of the target variable
   :type target: str
   :param custom_palette: Optional list of custom colors for visualization
   :type custom_palette: List[str], optional
   :raises ValueError: If more than 3 datasets are provided
   :return: None

   **Features:**

   - Creates side-by-side box plots and histograms for each numeric feature
   - Supports comparison of up to 3 datasets
   - Provides built-in color palettes inspired by nature:
     - Two datasets: Forest-themed green and yellow
     - Three datasets: Forest-themed green, yellow, and orange
   - Customizable color palette
   - Automatically excludes target variable from analysis

   **Example Usage:**

   .. code-block:: python

      from lunax.viz import numeric_eda

      # Basic usage
      numeric_eda([train_df, test_df], ['Train', 'Test'], target='target_column')

      # With custom colors
      numeric_eda([train_df, test_df], ['Train', 'Test'], 
                 target='target_column',
                 custom_palette=['#285185', '#D67940'])

.. py:function:: categoric_eda(df_list: List[pd.DataFrame], label_list: List[str], target: str, custom_palette: Optional[List[str]] = None) -> None

   Visualize the distribution of categorical features across different datasets.

   :param df_list: List of DataFrames to analyze
   :type df_list: List[pd.DataFrame]
   :param label_list: List of labels for each DataFrame
   :type label_list: List[str]
   :param target: Name of the target variable
   :type target: str
   :param custom_palette: Optional list of custom colors for visualization
   :type custom_palette: List[str], optional
   :raises ValueError: If more than 3 datasets are provided
   :return: None

   **Features:**

   - Creates pie charts and bar plots for each categorical feature
   - Supports comparison of up to 3 datasets
   - Uses the same nature-inspired color palettes as numeric_eda
   - Customizable color palette
   - Automatically excludes target variable from analysis
   - Pie charts show percentage distribution
   - Bar charts display absolute counts

   **Example Usage:**

   .. code-block:: python

      from lunax.viz import categoric_eda

      # Basic usage
      categoric_eda([train_df, test_df], ['Train', 'Test'], target='target_column')

      # With custom colors
      categoric_eda([train_df, test_df], ['Train', 'Test'], 
                   target='target_column',
                   custom_palette=['#FCA3B9', '#FCD752'])

Visualization Details
-------------------

Both functions create publication-quality visualizations with the following characteristics:

- Figure size: 12x4 inches
- DPI: 150
- Style: White grid background
- Automatic layout adjustment
- Clear titles and labels
- Legend for multiple datasets
- Consistent color schemes across plots

The visualizations are designed to provide immediate insights into data distributions and patterns while maintaining aesthetic appeal.