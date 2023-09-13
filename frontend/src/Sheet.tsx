import React from "react";
import "./Sheet.css";

export default class Sheet extends React.Component {
  render() {
    return (
      <div>
        <div className="CharacterSheet">
          <div className="attributes">
            <h1>
              <span className="attr-name">Attributes</span>
            </h1>
            <div className="attributes-box">
              <div className="spacer"></div>
              <div className="box-1">
                <h2>
                  Agility <button id="agi-value">0</button>
                </h2>

                <h2>
                  Brawn <button id="brawn-value">0</button>
                </h2>

                <h2>
                  Coordination <button id="coord-value">0</button>
                </h2>
              </div>
              <div className="spacer"></div>
              <div className="box-2">
                <h2>
                  Insight <button id="insight-value">0</button>
                </h2>

                <h2>
                  Gravitas <button id="gravi-value">0</button>
                </h2>

                <h2>
                  Reason <button id="reason-value">0</button>
                </h2>

                <h2>
                  Will <button id="will-value">0</button>
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
      </div>
    );
  }
}
