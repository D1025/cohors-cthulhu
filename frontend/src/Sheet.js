import React from "react";
import "./Sheet.css";

export default class Sheet extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            agi: 0,
            brawn: 0,
            coord: 0,
            insight: 0,
            gravitas: 0,
            reason: 0,
            will: 0,
        };
        this.sendState = this.sendState.bind(this);
    }

    sendState(e) {
        let value = e.target.value;
        let attribute = e.target.innerHTML.split(" ")[0];
        let message = {
            type: "attribute",
            nickname: this.props.nickname,
            attribute: attribute,
            value: value
        }
        this.props.ws.send(JSON.stringify(message))
    }

    render() {
        return (<div>
            <div className="CharacterSheet">
                <div className="attributes">
                    <h1>
                        <span className="attr-name">Attributes</span>
                    </h1>
                    <div className="attributes-box">
                        <div className="spacer"></div>
                        <div className="box-1">
                            <h2>
                                <button
                                    onClick={this.sendState}
                                    id="agi-value"
                                    className="button"
                                    value={this.state.agi}
                                >
                                    Agility <span>{this.state.agi}</span>
                                </button>
                            </h2>

                            <h2>
                                <button
                                    onClick={this.sendState}
                                    id="brawn-value"
                                    className="button"
                                    value={this.state.brawn}>
                                    Brawn<span> {this.state.brawn} </span>
                                </button>
                            </h2>

                            <h2>
                                <button
                                    onClick={this.sendState}
                                    id="coord-value"
                                    className="button"
                                    value={this.state.coord}
                                >
                                    Coordination <span>{this.state.coord}</span>
                                </button>
                            </h2>
                        </div>
                        <div className="spacer"></div>
                        <div className="box-2">
                            <h2>
                                <button
                                    onClick={this.sendState}
                                    id="insight-value"
                                    className="button"
                                    value={this.state.insight}
                                >
                                    Insight <span>{this.state.insight}</span>
                                </button>
                            </h2>

                            <h2>
                                <button
                                    onClick={this.sendState}
                                    id="gravi-value"
                                    className="button"
                                    value={this.state.gravitas}
                                >
                                    Gravitas <span>{this.state.gravitas}</span>
                                </button>
                            </h2>

                            <h2>
                                <button
                                    onClick={this.sendState}
                                    id="reason-value"
                                    className="button"
                                    value={this.state.reason}
                                >
                                    Reason <span>{this.state.reason}</span>
                                </button>
                            </h2>

                            <h2>
                                <button
                                    onClick={this.sendState}
                                    id="will-value"
                                    className="button"
                                    value={this.state.will}
                                >
                                    Will <span>{this.state.will}</span>
                                </button>
                            </h2>
                        </div>
                        <div className="spacer"></div>
                    </div>
                </div>
                <div className="skills">
                    <h1>
                        <span className="attr-name">Skills</span>
                    </h1>
                    <div className="skills-box">
                        <div className="box-1">
                            <h2>
                                <button id="academia">Academia</button>
                            </h2>
                        </div>
                        <div className="box-2"></div>
                        <h2>
                            <button id="Stealth">Stealth</button>
                        </h2>
                    </div>
                </div>
            </div>
        </div>);
    }
}
