import React, { Component } from 'react';

import Header from './Components/Header';

import ProductBox from './Components/Product';

class App extends Component {
  render() {
    return (
      <div className="container">
        <Header title="Products App" />
        <br />
        <ProductBox />
      </div>
    );
  }
}

export default App;