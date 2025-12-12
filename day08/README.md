# day 8: ml model deployment: microservice mission

## focus: fastai + pytorch

hi guys. here's an overview of your tasks for today. 

you'll be learning about **model deployment and practices**. the goal is to take a saved ml model and wrap it into a callable microservice using an **api** (specifically, **fastapi**).

think of it as isolating the *brain* (the model) so it can handle prediction requests fast and scale easily. 
## **your checklist:**


1.  **the model:** assume you have `model.pt` (a pytorch model file) ready to go. 
2.  **the server (`main.py`):**
      * init a `fastapi` app.
      * **hot load:** the model **must** load only **once** when the server **starts up**. no reloading on every request, that's slow. use `torch.load` and remember to set it to `.eval()`.
      * **the route:** define a `post` endpoint at `/predict`. this is where the magic happens.
          * it takes some input data (json is standard).
          * convert that input into a **pytorch tensor**.
          * pass it through the model.
          * send the prediction result back as a simple json response.
3.  **dependencies:** a tidy `requirements.txt` (you'll need `fastapi`, `uvicorn`, `torch`, and `pydantic`).
4.  **data check:** use **pydantic** to define what the input data *should* look like. saves a ton of headache later.

## **crash course:**

  * **fastapi 101:** the best way is to explore projects that use fastapi, and when you come across a function/class you haven't heard of before, look up the documentation. 
      * **basics:** defining routes and the whole `uvicorn` setup.
      * **input data:** how to use `pydantic` for request bodies.
      * [FastAPI Crash Course](https://www.youtube.com/watch?v=nWWPlEO0he8): watch this 40 min video, explains fast-api basics. 
        
  * **deploying ml models using fastapi:** in this video, they deploy a scikit-learn based RandomForestClassifier trained on the UCI banknote authentication dataset. watch this to get an idea: [How To Deploy Machine Learning Models Using FastAPI](https://www.youtube.com/watch?v=b5F667g1yCk)
        
  * **saving and loading models in pytorch:** for this, you can either use any pre-existing pytorch model from the previous day that you may have, or code up any simple model and use that.
      * loading: you'll use `torch.load('model.pt')`. make sure you know the difference between loading the whole thing vs. just the weights (we're assuming the whole thing here for speed). watch this video on [how to load and save pytorch models](https://www.youtube.com/watch?v=9L9jEOwRrCg&t=175s)
     
      * **persistence:** read about how you can prevent your model's weights from reloading on every API call and minimize latency, the core concept is to load the model into memory once when the server application starts up and keep it globally accessible for all subsequent requests.
        
        

  * **reading material:** optional, but read a quick blog on "ml model serving architecture". it'll explain why separating the model as a dedicated service is the pro move (decoupling, scaling, efficiency). [blog: ml model serving architecture](https://medium.com/decodingai/ml-serving-101-core-architectures-cf8cbb852aa8)

## **some useful stuff:**

  * **startup:** fastapi has a special hook for stuff that should only run once: `@app.on_event("startup")`. that's your model load spot.
    ```python
    @app.on_event("startup")
    async def load_our_brain():
        global ml_model
        # load model, assign to ml_model, call .eval()
        print("model is live!")
    ```
  * **prediction logic:** for the `/predict` function:
      * wrap the inference code in `with torch.no_grad():` you don't need gradients for predicting, so this saves memory/time.
      * remember to convert the incoming data to a tensor (`torch.tensor(data).float()`) and the final output *back* to a python type (`.tolist()` or `.item()`) before returning.


## **final submission file**

  * your pr needs to include these files showing you created a FastAPI server **(main.py)** that loads `model.pt` at startup, uses Pydantic for input validation, and exposes a working `/predict` POST endpoint.
