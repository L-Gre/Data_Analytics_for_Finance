

Terminology
-----------
> \
> `Target variable` (a.k.a. `dependent` variable, `output` variable, `label`)
>   * what you are trying to predict or estimate
>
> `Input variable` (a.k.a. `independent` variable, `explanatory` variable, `predictor`, `feature`)
>   * input variables or features that influence the dependent variable
>       

How the model learns (training vs. test)
----------------------------------------

### Splitting Data
* For a ML model to learn, you need to `split` your data into a `training set` and a `test set`.
    * example data set: 
        * 1 target variable (e.g. liquidity)
        * 5 explanatory variables (e.g. market cap, dept, ebitda, etc.)
        * 100,000 observations

### Training
* When `'training'` the model, the model will review the given `'characteristics'` (input variables) present AND the `'thing'` (target variable) you're trying to predict at a later stage
    * "When the Liquidity (target variable) value was 3884, 'market cap' was 41645, 'total debt' was 9040, ... etc.
* You train the model on `~80%` of your available data (a.k.a. `output variable **AND** input variables`)
    * You show it 80,000 `output:input pairs`, i.e. liquidity and values of 5 input variables x80,000

### Testing
* Once complete, the model should now be able to make `predictions` on what the `target variable SHOULD be`, given a set of 'characteristics' (input variables) 
    * You show the model another observation of the 5 input variables, it should now be able to predict liquidity (the output value)
* You can `'test'` this by feeding the model the remaining `~20%` of characteristics (input variables) you previously reserved and recording the output value the model predicts
* You can now compare the answers the model gave (the values it predicted) to the actual remaining ~20% answers (output values) you previously reserved (which the model hasn't seen, so doesn't know this answer)
* This will determine the models `accuracy`


Model Competition
-----------------

> May the best model class win!

Prior to competition, define process (a.k.a. `model pipeline`!) repeated for each `model class`:

Liquidity regressor algorithm = 2-step pipeline!
1. `standardise` training data to common scale
2. `apply model class` to training data w/ a given random state

> N.B. Standardising data to common scale prevents MLA from overemphasising input features with larger scale. Without this step, input features with larger values could have greater influence on your model!