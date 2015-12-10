# Installation

This code has been tested with Python 2.7.11

First create a virtual environment 

    $: pyenv versions
      system
      2.7.11rc1
      3.5.0
    $: pyenv virtualenv 2.7.11rc1 k_means
    $: pip install -r requirements.txt

You can now load your KMeans code in a console:

    >>> import imp  
    >>> k_means = imp.load_source('k_means', 'lib/k_means.py')  
    >>> data = np.array([  
      [1, 1],  
      [2, 2],  
      [3, 3],  
      [10, 10],  
      [11, 11],  
      [12, 12]  
    ])  
    >>> k_means.KMeans(data, 2).fit()  
    [Cluster(center=[ 11.  11.], members=[array([10, 10]), array([11, 11]), array([12, 12])], converged=True), Cluster(center=[ 2.  2.], members=[array([1, 1]), array([2, 2]), array([3, 3])], converged=True)]


Alternatively you can download the tar in the dist folder, extract it and install it with

    $: python setup.py install


# Running the tests

    py.test

