import React, { Component } from 'react';

class App extends Component {
  state = {
    Category: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://15.165.77.159:8002/charts/');
      const posts = await res.json();
      console.log(posts);
      this.setState({
        Category: posts
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
        <div>
          {this.state.Category.map(item => (
              <div key={item.ticker2}>
                <h1>{item.category_name}</h1>
                <span>{item.category_ticker}</span>
              </div>
          ))}
        </div>
    );
  }
}

export default App;
