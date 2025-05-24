树模型
==========

本模块包含了多种树模型的封装类，包括XGBoost、LightGBM和CatBoost的回归和分类模型。

XGBoost模型
-----------

.. py:class:: xgb_reg(params: Optional[Dict] = None)

   XGBoost回归模型封装类。

   :param params: XGBoost模型的超参数字典
   :type params: Dict, optional

   .. py:method:: fit(X: pd.DataFrame, y: pd.Series, k_fold: Optional[int] = None) -> None

      训练模型，支持k折交叉验证。

      :param X: 特征数据
      :param y: 目标变量
      :param k_fold: 交叉验证折数，默认为None（不使用交叉验证）

   .. py:method:: predict(X: pd.DataFrame) -> np.ndarray

      预测新数据。

      :param X: 特征数据
      :return: 预测结果

   .. py:method:: evaluate(X: pd.DataFrame, y: pd.Series, log_info: bool = True) -> Dict[str, float]

      评估模型性能。

      :param X: 特征数据
      :param y: 真实标签
      :param log_info: 是否打印评估信息
      :return: 评估指标字典

.. py:class:: xgb_clf(params: Optional[Dict] = None)

   XGBoost分类模型封装类。

   :param params: XGBoost模型的超参数字典
   :type params: Dict, optional

   .. py:method:: fit(X: pd.DataFrame, y: pd.Series, k_fold: Optional[int] = None) -> None

      训练模型，支持k折交叉验证。

      :param X: 特征数据
      :param y: 目标变量
      :param k_fold: 交叉验证折数，默认为None（不使用交叉验证）

   .. py:method:: predict(X: pd.DataFrame) -> np.ndarray

      预测新数据。

      :param X: 特征数据
      :return: 预测结果

   .. py:method:: predict_proba(X: pd.DataFrame) -> np.ndarray

      预测类别概率。

      :param X: 特征数据
      :return: 预测概率

   .. py:method:: evaluate(X: pd.DataFrame, y: pd.Series, log_info: bool = True) -> Dict[str, float]

      评估模型性能。

      :param X: 特征数据
      :param y: 真实标签
      :param log_info: 是否打印评估信息
      :return: 评估指标字典

LightGBM模型
------------

.. py:class:: lgbm_reg(params: Optional[Dict] = None)

   LightGBM回归模型封装类。

   :param params: LightGBM模型的超参数字典
   :type params: Dict, optional

   .. py:method:: fit(X: pd.DataFrame, y: pd.Series, k_fold: Optional[int] = None) -> None

      训练模型，支持k折交叉验证。

      :param X: 特征数据
      :param y: 目标变量
      :param k_fold: 交叉验证折数，默认为None（不使用交叉验证）

   .. py:method:: predict(X: pd.DataFrame) -> np.ndarray

      预测新数据。

      :param X: 特征数据
      :return: 预测结果

   .. py:method:: evaluate(X: pd.DataFrame, y: pd.Series, log_info: bool = True) -> Dict[str, float]

      评估模型性能。

      :param X: 特征数据
      :param y: 真实标签
      :param log_info: 是否打印评估信息
      :return: 评估指标字典

.. py:class:: lgbm_clf(params: Optional[Dict] = None)

   LightGBM分类模型封装类。

   :param params: LightGBM模型的超参数字典
   :type params: Dict, optional

   .. py:method:: fit(X: pd.DataFrame, y: pd.Series, k_fold: Optional[int] = None) -> None

      训练模型，支持k折交叉验证。

      :param X: 特征数据
      :param y: 目标变量
      :param k_fold: 交叉验证折数，默认为None（不使用交叉验证）

   .. py:method:: predict(X: pd.DataFrame) -> np.ndarray

      预测新数据。

      :param X: 特征数据
      :return: 预测结果

   .. py:method:: predict_proba(X: pd.DataFrame) -> np.ndarray

      预测类别概率。

      :param X: 特征数据
      :return: 预测概率

   .. py:method:: evaluate(X: pd.DataFrame, y: pd.Series, log_info: bool = True) -> Dict[str, float]

      评估模型性能。

      :param X: 特征数据
      :param y: 真实标签
      :param log_info: 是否打印评估信息
      :return: 评估指标字典

CatBoost模型
------------

.. py:class:: cat_reg(params: Optional[Dict] = None)

   CatBoost回归模型封装类。

   :param params: CatBoost模型的超参数字典
   :type params: Dict, optional

   .. py:method:: fit(X: pd.DataFrame, y: pd.Series, k_fold: Optional[int] = None) -> None

      训练模型，支持k折交叉验证。

      :param X: 特征数据
      :param y: 目标变量
      :param k_fold: 交叉验证折数，默认为None（不使用交叉验证）

   .. py:method:: predict(X: pd.DataFrame) -> np.ndarray

      预测新数据。

      :param X: 特征数据
      :return: 预测结果

   .. py:method:: evaluate(X: pd.DataFrame, y: pd.Series, log_info: bool = True) -> Dict[str, float]

      评估模型性能。

      :param X: 特征数据
      :param y: 真实标签
      :param log_info: 是否打印评估信息
      :return: 评估指标字典

.. py:class:: cat_clf(params: Optional[Dict] = None)

   CatBoost分类模型封装类。

   :param params: CatBoost模型的超参数字典
   :type params: Dict, optional

   .. py:method:: fit(X: pd.DataFrame, y: pd.Series, k_fold: Optional[int] = None) -> None

      训练模型，支持k折交叉验证。

      :param X: 特征数据
      :param y: 目标变量
      :param k_fold: 交叉验证折数，默认为None（不使用交叉验证）

   .. py:method:: predict(X: pd.DataFrame) -> np.ndarray

      预测新数据。

      :param X: 特征数据
      :return: 预测结果

   .. py:method:: predict_proba(X: pd.DataFrame) -> np.ndarray

      预测类别概率。

      :param X: 特征数据
      :return: 预测概率

   .. py:method:: evaluate(X: pd.DataFrame, y: pd.Series, log_info: bool = True) -> Dict[str, float]

      评估模型性能。

      :param X: 特征数据
      :param y: 真实标签
      :param log_info: 是否打印评估信息
      :return: 评估指标字典