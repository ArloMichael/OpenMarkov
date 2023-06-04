# OpenMarkov

A Python module for generating text with Markov chains

## Installation

Clone the GitHub repository to your local machine:

``` console
git clone https://github.com/ArloMichael/OpenMarkov.git
```

## Usage

1.  Import the `Chain` class from the module:
   
``` python
from markov import Chain
```

2.  Create an instance of the `Chain` class with an optional `order` parameter to specify the order of the Markov chain (default is 1):

``` python
chain = Chain(order=2)
```

3.  Train the Markov chain by providing a text corpus using the `train` method:

``` python
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce interdum orci vitae massa efficitur finibus. Nunc nulla massa, malesuada elementum porta at, blandit et erat. Vivamus auctor vehicula libero nec ornare. Donec in eros nulla. Cras a interdum dolor, at viverra enim. Nam cursus nunc dignissim, blandit ex id, commodo tellus. Integer fringilla tortor id tellus egestas vehicula." 
chain.train(text)
```

4.  Generate text using the `generate` method. Specify the desired length of the generated text with the `length` parameter (default is 10). You can also provide an optional `seed` parameter to set the initial prefix:

``` python
generated_text = chain.generate(length=20, seed="Lorem ipsum")
print(generated_text)
```

5.  Save the trained Markov chain to a JSON file using the `save` method:

``` python
chain.save("model.json")
```

6.  Load a saved Markov chain from a JSON file using the `load` class method:

``` python
chain = Chain.load("model.json")
```

## Example

Here's a complete example demonstrating the usage of the Markov chain text generator:

``` python
from markov import Chain  

# Create an instance of the Chain class
chain = Chain(order=2)

# Train the Markov chain
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lacinia augue vitae consequat fermentum."
chain.train(text)

# Generate text
generated_text = chain.generate(length=20, seed="Lorem ipsum")
print(generated_text)

# Save the Markov chain
chain.save("model.json")

# Load a saved Markov chain
loaded_chain = Chain.load("model.json")
```
