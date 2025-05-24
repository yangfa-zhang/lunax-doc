lunax.viz
=================

This module provides visualization tools for exploratory data analysis (EDA).

.. py:module:: lunax.viz.eda

Functions for visualizing data distributions and patterns.

.. py:function:: numeric_eda(df_list: List[pd.DataFrame], label_list: List[str], target: str, custom_palette: Optional[List[str]] = None) -> None

   Create visualization for numeric features distribution.

   :param df_list: List of DataFrames to analyze
   :type df_list: List[pd.DataFrame]
   :param label_list: List of labels for each DataFrame
   :type label_list: List[str]
   :param target: Name of target variable
   :type target: str
   :param custom_palette: Custom color palette for visualization
   :type custom_palette: List[str], optional
   :raises ValueError: If more than 3 datasets are provided
   :return: None

   Creates two subplots for each numeric feature:
      - Box plot showing distribution comparison
      - Histogram with kernel density estimation

   **Default Color Palettes:**

   For two datasets:
      - Forest theme: ``["#5A8100", "#FFB400"]`` (Green, Yellow)
      - Ocean theme: ``['#B74803','#022E51']`` (Brown, Navy)
      - Mountain theme: ``["#C7A003", "#3D4E17"]`` (Gold, Olive)
      - Fashion theme: ``["#FCA3B9","#FCD752"]`` (Pink, Yellow)
      - Classic theme: ``["#285185","#D67940"]`` (Blue, Orange)

   For three datasets:
      - Forest theme: ``["#5A8100", "#FFB400", "#FF6C02"]`` (Green, Yellow, Orange)
      - Mountain theme: ``["#C7A003", "#3D4E17", "#151F1E"]`` (Gold, Olive, Dark)

.. py:function:: categoric_eda(df_list: List[pd.DataFrame], label_list: List[str], target: str, custom_palette: Optional[List[str]] = None) -> None

   Create visualization for categorical features distribution.

   :param df_list: List of DataFrames to analyze
   :type df_list: List[pd.DataFrame]
   :param label_list: List of labels for each DataFrame
   :type label_list: List[str]
   :param target: Name of target variable
   :type target: str
   :param custom_palette: Custom color palette for visualization
   :type custom_palette: List[str], optional
   :raises ValueError: If more than 3 datasets are provided
   :return: None

   Creates two subplots for each categorical feature:
      - Pie chart showing proportion distribution
      - Bar chart showing count distribution

   Uses the same color palettes as :func:`numeric_eda`

Example Usage
------------

.. code-block:: python

   from lunax.viz import numeric_eda, categoric_eda

   # Basic usage
   numeric_eda([train_df, test_df], ['Train', 'Test'], target='target')
   categoric_eda([train_df, test_df], ['Train', 'Test'], target='target')

   # With custom color palette
   custom_colors = ['#285185', '#D67940']
   numeric_eda([train_df, test_df], ['Train', 'Test'], 
               target='target', custom_palette=custom_colors)