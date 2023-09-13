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
                  <button id="agi-value" className="button">
                    Agility <span>0</span>
                  </button>
                </h2>

                <h2>
                  <button id="brawn-value" className="button">
                    Brawn<span>0</span>
                  </button>
                </h2>

                <h2>
                  <button id="coord-value" className="button">
                    Coordination <span>0</span>
                  </button>
                </h2>
              </div>
              <div className="spacer"></div>
              <div className="box-2">
                <h2>
                  <button id="insight-value" className="button">
                    Insight <span>0</span>
                  </button>
                </h2>

                <h2>
                  <button id="gravi-value" className="button">
                    Gravitas <span>0</span>
                  </button>
                </h2>

                <h2>
                  <button id="reason-value" className="button">
                    Reason <span>0</span>
                  </button>
                </h2>

                <h2>
                  <button id="will-value" className="button">
                    Will <span>0</span>
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
      </div>
    );
  }
}
