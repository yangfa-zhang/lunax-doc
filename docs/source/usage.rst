Usage
=====

.. _installation:

Installation
------------

To use lunax, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lunax

Data Preprocessing
------------------
For example: 

.. code-block:: python

   from lunax.data_processing import *
   df_train = load_data('train.csv') # or df = load_data('train.parquet',mode='parquet')
   target = 'label_column_name'
   df_train = preprocess_data(df_train, target)

Exploratory Data Analysis
-------------------------
For example:

.. code-block:: python

   from lunax.viz import numeric_eda, categoric_eda
   numeric_eda([df_train,df_test],['train','test'],target=target) # numeric feature analysis
   categoric_eda([df_train,df_test],['train','test'],target=target) # categorical feature analysis

Modeling
---------
For example:

.. code-block:: python

   from lunax.models import xgb_clf # or xgb_reg, lgbm_reg, lgbm_clf, cat_clf, cat_reg
   from lunax.hyper_opt import OptunaTuner
   tuner = OptunaTuner(n_trials=10,model_class="XGBClassifier") # Hyperparameter optimizer, n_trials is the number of optimization times
   # or "XGBRegressor", "LGBMRegressor", "LGBMClassifier" , "CatClassifier", "CatRegressor"
   X_train, X_val, y_train, y_val = split_data(df_train, target)
   results = tuner.optimize(X_train, y_train, X_val, y_val)
   best_params = results['best_params']
   model = xgb_clf(best_params)
   model.fit(X_train, y_train)

Model Evaluation and Explainable AI (XAI)
------------------------------------------

.. code-block:: python

   model.evaluate(X_val, y_val)

Ensemble Learning
-----------------

.. code-block:: python

   from lunax.ensembles import HillClimbingEnsemble
   model1 = xgb_clf()
   model2 = lgbm_clf()
   model3 = cat_clf()
   for model in [model1, model2, model3]:
      model.fit(X_train, y_train)
   ensemble = HillClimbingEnsemble(
      models=[model1, model2, model3],
      metric=['auc'],
      maximize=True
   )
   best_weights = ensemble.fit(X_val, y_val)
   predictions = ensemble.predict(df_test)