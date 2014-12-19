{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Test notebook"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This is a text notebook. Here *are* some **rich text**, `code`, $\\pi\\simeq 3.14$ equations."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Python code:\n",
    "\n",
    "```python\n",
    "# some code in python\n",
    "```\n",
    "\n",
    "Random code (no syntax highlight):\n",
    "\n",
    "```\n",
    "# some random code 1\n",
    "```\n",
    "\n",
    "Random code:\n",
    "\n",
    "    some random code 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Two paragraphs.\n",
    "\n",
    "In a single cell."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import IPython"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "2*2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "3*3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "some text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "16\n"
     ]
    }
   ],
   "source": [
    "print(4*4)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "An image:\n",
    "\n",
    "![Hello world](http://wristgeek.com/wp-content/uploads/2014/09/hello_world.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Subtitle\n",
    "\n",
    "a list\n",
    "\n",
    "* One [small](http://www.google.fr) link!\n",
    "* Two"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "and"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. Un\n",
    "2. Deux"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.image.AxesImage at 0x7fe9ab214c50>"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": [
       "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\n"
      ],
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7fe9ab2d4080>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.imshow(np.random.rand(5,5,4), interpolation='none')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "That's all folks."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "IPython (Python 3)",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.4.2"
  },
  "signature": "sha256:4e5212546d3d40e6d8840f06b0e019c260e48fe526a35279729789b65eac1282"
 },
 "nbformat": 4,
 "nbformat_minor": 0
}