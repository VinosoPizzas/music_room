import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";

//renderiza tudo a partir do HomePage.js
export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className="center">
                <HomePage />
            </div>
        );
    }
}

//renderiza os elementos dessa página no index.html 
const appDiv = document.getElementById("app");
render(<App />, appDiv);