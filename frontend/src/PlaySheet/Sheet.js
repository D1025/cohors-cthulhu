import React from "react";
import "./Sheet.css";

export default class Sheet extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: "",
      agi: 0,
      agiChecked: false,
      brawn: 0,
      brawnChecked: false,
      coord: 0,
      coordChecked: false,
      insight: 0,
      insightChecked: false,
      gravitas: 0,
      gravitasChecked: false,
      reason: 0,
      reasonChecked: false,
      will: 0,
      willChecked: false,
      academia: 0,
      academiaChecked: false,
      athletics: 0,
      athleticsChecked: false,
      crafting: 0,
      craftingChecked: false,
      engineering: 0,
      engineeringChecked: false,
      fighting: 0,
      fightingChecked: false,
      medicine: 0,
      medicineChecked: false,
      observation: 0,
      observationChecked: false,
      persuasion: 0,
      persuasionChecked: false,
      resilience: 0,
      resilienceChecked: false,
      stealth: 0,
      stealthChecked: false,
      survival: 0,
      survivalChecked: false,
      tactics: 0,
      tacticsChecked: false,
      focusChecked: false,
      dice: 1,
      data: null,
      isLoading: true,
      error: null,
      editFocuses: false,
      editTruths: false,
      editTalents: false,
    };
    this.buttonClickedAttr = this.buttonClickedAttr.bind(this);
    this.buttonClickedSkill = this.buttonClickedSkill.bind(this);
    this.handleFocusChange = this.handleFocusChange.bind(this);
    this.handleEditFocuses = this.handleEditFocuses.bind(this);
    this.handleEditTruths = this.handleEditTruths.bind(this);
  }
  apiURL = process.env.REACT_APP_PROD === 'true'
? "http://localhost:8086"
: "http://104.248.37.81:8086";

  buttonClickedAttr(e) {
    const attributeMapping = {
      Agility: "agiChecked",
      Brawn: "brawnChecked",
      Coordination: "coordChecked",
      Insight: "insightChecked",
      Gravitas: "gravitasChecked",
      Reason: "reasonChecked",
      Will: "willChecked",
    };
    let attribute = e.target.innerHTML.split(" ")[0];
    let stateKey = attributeMapping[attribute];

    if (stateKey) {
      this.setState((prevState) => ({
        agiChecked: false,
        brawnChecked: false,
        coordChecked: false,
        insightChecked: false,
        gravitasChecked: false,
        reasonChecked: false,
        willChecked: false,
        [stateKey]: !prevState[stateKey],
      }));
    }
  }
  buttonClickedSkill(e) {
    const skillMapping = {
      academia: "academiaChecked",
      athletics: "athleticsChecked",
      crafting: "craftingChecked",
      engineering: "engineeringChecked",
      fighting: "fightingChecked",
      medicine: "medicineChecked",
      observation: "observationChecked",
      persuasion: "persuasionChecked",
      resilience: "resilienceChecked",
      stealth: "stealthChecked",
      survival: "survivalChecked",
      tactics: "tacticsChecked",
    };

    let skillName = e.target.innerHTML.split(" ")[0];
    let stateKey = skillMapping[skillName];

    if (stateKey) {
      this.setState((prevState) => ({
        academiaChecked: false,
        athleticsChecked: false,
        craftingChecked: false,
        engineeringChecked: false,
        fightingChecked: false,
        medicineChecked: false,
        observationChecked: false,
        persuasionChecked: false,
        resilienceChecked: false,
        stealthChecked: false,
        survivalChecked: false,
        tacticsChecked: false,
        [stateKey]: !prevState[stateKey],
      }));
    }
  }
  handleFocusChange = () => {
    this.setState((prevState) => ({
      focusChecked: !prevState.focusChecked,
    }));
  };
  handleSubmitRoll = () => {
    const attributeMapping = {
      agility: { checked: this.state.agiChecked, value: this.state.agi },
      brawn: { checked: this.state.brawnChecked, value: this.state.brawn },
      coordination: {
        checked: this.state.coordChecked,
        value: this.state.coord,
      },
      insight: {
        checked: this.state.insightChecked,
        value: this.state.insight,
      },
      gravitas: {
        checked: this.state.gravitasChecked,
        value: this.state.gravitas,
      },
      reason: { checked: this.state.reasonChecked, value: this.state.reason },
      will: { checked: this.state.willChecked, value: this.state.will },
    };

    const skillMapping = {
      academia: {
        checked: this.state.academiaChecked,
        value: this.state.academia,
      },
      athletics: {
        checked: this.state.athleticsChecked,
        value: this.state.athletics,
      },
      crafting: {
        checked: this.state.craftingChecked,
        value: this.state.crafting,
      },
      engineering: {
        checked: this.state.engineeringChecked,
        value: this.state.engineering,
      },
      fighting: {
        checked: this.state.fightingChecked,
        value: this.state.fighting,
      },
      medicine: {
        checked: this.state.medicineChecked,
        value: this.state.medicine,
      },
      observation: {
        checked: this.state.observationChecked,
        value: this.state.observation,
      },
      persuasion: {
        checked: this.state.persuasionChecked,
        value: this.state.persuasion,
      },
      resilience: {
        checked: this.state.resilienceChecked,
        value: this.state.resilience,
      },
      stealth: {
        checked: this.state.stealthChecked,
        value: this.state.stealth,
      },
      survival: {
        checked: this.state.survivalChecked,
        value: this.state.survival,
      },
      tactics: {
        checked: this.state.tacticsChecked,
        value: this.state.tactics,
      },
    };

    let attribute = "";
    let attrVal = 0;
    for (let key in attributeMapping) {
      if (attributeMapping[key].checked) {
        attribute = key;
        attrVal = attributeMapping[key].value;
        break;
      }
    }

    if (!attribute) {
      alert("No attribute checked");
      return;
    }

    let skill = "";
    let skillVal = 0;
    for (let key in skillMapping) {
      if (skillMapping[key].checked) {
        skill = key;
        skillVal = skillMapping[key].value;
        break;
      }
    }

    if (!skill) {
      skill = "blank";
      skillVal = 0;
    }

    let message = {
      type: "roll",
      nickname: this.props.nickname,
      dice: this.state.dice,
      focus: this.state.focusChecked,
      attribute: attribute,
      attributeValue: attrVal,
      skill: skill,
      skillValue: skillVal,
    };
    this.props.ws.send(JSON.stringify(message));
  };

  handledice = (e) => {
    this.setState((prevState) => ({
      dice: parseInt(e.target.value),
    }));
  };
  componentDidMount() {
    
    fetch(this.apiURL + `/character?name=${this.props.nickname}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        this.setState({
          agi: data.attributes.agility | 0,
          brawn: data.attributes.brawn | 0,
          coord: data.attributes.coordination | 0,
          insight: data.attributes.insight | 0,
          gravitas: data.attributes.gravitas | 0,
          reason: data.attributes.reason | 0,
          will: data.attributes.will | 0,
          academia: data.skills.academia | 0,
          athletics: data.skills.athletics | 0,
          crafting: data.skills.crafting | 0,
          engineering: data.skills.engineering | 0,
          fighting: data.skills.fighting | 0,
          medicine: data.skills.medicine | 0,
          observation: data.skills.observation | 0,
          persuasion: data.skills.persuasion | 0,
          resilience: data.skills.resilience | 0,
          stealth: data.skills.stealth | 0,
          survival: data.skills.survival | 0,
          tactics: data.skills.tactics | 0,
          data: data,
          isLoading: false, // Update isLoading to false
          error: null,
        });
      })
      .catch((error) => {
        console.error("API Error:", error); // Log any error
        this.setState({
          error: error,
          isLoading: false,
        });
      });
  }

  handleInputChange = (event) => {
    this.setState({ input: event.target.value });
  };
  handleEnterPress = (e) => {
    if (e.key === "Enter") {
      this.handleAddTruth();
    }
  };
  handleAddTruth = () => {
    const message = {
      nickname: this.props.nickname,
      type: "truth",
      message: this.state.input,
    };
    this.props.ws.send(JSON.stringify(message));
  };
  handleStress = (e) => {
    let message = {
      type: "stress",
      message: e.target.value,
    };
    this.props.ws.send(JSON.stringify(message));
  };
  handleEditFocuses() {
    this.setState({
      editFocuses: !this.state.editFocuses,
    });
  }
  handleEditTruths() {
    this.setState({
      editTruths: !this.state.editTruths,
    });
  }
  handleDeleteTruth(itemID) {
    const message = {
      nickname: this.props.nickname,
      type: "delete",
      itemType: "truth",
      itemID: itemID,
    };
    this.props.ws.send(JSON.stringify(message));
    // Refresh the React page
    const url = "/?nickname=" + this.props.nickname;
    window.location.href = url;
  }
  handleDeleteFocus(itemID) {
    const message = {
      nickname: this.props.nickname,
      type: "delete",
      itemType: "focus",
      itemID: itemID,
    };
    this.props.ws.send(JSON.stringify(message));

    // Refresh the React page
    window.location.reload();
    const url = "/?nickname=" + this.props.nickname;
    window.location.href = url;
  }
  render() {
    return (
      <div>
        {!this.state.isLoading ? (
          <div className={"entire"}>
            <div className="CharacterSheet">
              <div className="hp">
                <label htmlFor="stress">
                  Enter stress(0/
                  {this.state.data !== null ? this.state.data.maxStress : 0}):
                </label>
                <input
                  onChange={this.handleStress}
                  type={"number"}
                  name={"stress"}
                  min={"0"}
                  max={
                    this.state.data !== null ? this.state.data.maxStress | 0 : 0
                  }
                />
              </div>
              <div className={"momentum-threat"}>
                Momentum:{" "}
                {this.state.data !== null ? (
                  this.state.data.momentum | 0
                ) : (
                  <span>bad nickname</span>
                )}{" "}
                Threat:{" "}
                {this.state.data !== null ? (
                  this.state.data.threat | 0
                ) : (
                  <span>bad nickname</span>
                )}
              </div>
              <div className="attributes">
                <h1>
                  <span className="attr-name">Attributes</span>
                </h1>
                <div className="attributes-box">
                  <div className="box-1">
                    <h2>
                      <button
                        onClick={this.buttonClickedAttr}
                        id="agi-value"
                        className={
                          this.state.agiChecked ? "button checked" : "button"
                        }
                      >
                        Agility <span>{this.state.agi}</span>
                      </button>
                    </h2>

                    <h2>
                      <button
                        onClick={this.buttonClickedAttr}
                        id="brawn-value"
                        className={
                          this.state.brawnChecked ? "button checked" : "button "
                        }
                      >
                        Brawn <span>{this.state.brawn}</span>
                      </button>
                    </h2>

                    <h2>
                      <button
                        onClick={this.buttonClickedAttr}
                        id="coord-value"
                        className={
                          this.state.coordChecked ? "button checked" : "button "
                        }
                      >
                        Coordination <span>{this.state.coord}</span>
                      </button>
                    </h2>
                  </div>
                  <div className="spacer"></div>
                  <div className="box-2">
                    <h2>
                      <button
                        onClick={this.buttonClickedAttr}
                        id="insight-value"
                        className={
                          this.state.insightChecked
                            ? "button checked"
                            : "button "
                        }
                      >
                        Insight <span>{this.state.insight}</span>
                      </button>
                    </h2>

                    <h2>
                      <button
                        onClick={this.buttonClickedAttr}
                        id="gravi-value"
                        className={
                          this.state.gravitasChecked
                            ? "button checked"
                            : "button "
                        }
                      >
                        Gravitas <span>{this.state.gravitas}</span>
                      </button>
                    </h2>

                    <h2>
                      <button
                        onClick={this.buttonClickedAttr}
                        id="reason-value"
                        className={
                          this.state.reasonChecked
                            ? "button checked"
                            : "button "
                        }
                      >
                        Reason <span>{this.state.reason}</span>
                      </button>
                    </h2>

                    <h2>
                      <button
                        onClick={this.buttonClickedAttr}
                        id="will-value"
                        className={
                          this.state.willChecked ? "button checked" : "button "
                        }
                      >
                        Will <span>{this.state.will}</span>
                      </button>
                    </h2>
                  </div>
                </div>
              </div>
              <div className="skills">
                <h1>
                  <span className="attr-name">Skills</span>
                </h1>
                <div className="skills-box">
                  <div className="box-1">
                    <h2>
                      <button
                        onClick={this.buttonClickedSkill}
                        className={
                          this.state.academiaChecked
                            ? "button checked"
                            : "button "
                        }
                        value={this.state.academia}
                        id="academia"
                      >
                        academia <span>{this.state.academia}</span>
                      </button>
                    </h2>

                    <h2>
                      <button
                        onClick={this.buttonClickedSkill}
                        className={
                          this.state.athleticsChecked
                            ? "button checked"
                            : "button "
                        }
                        value={this.state.athletics}
                        id="athletics"
                      >
                        athletics <span>{this.state.athletics}</span>
                      </button>
                    </h2>
                    <h2>
                      <button
                        onClick={this.buttonClickedSkill}
                        className={
                          this.state.craftingChecked
                            ? "button checked"
                            : "button "
                        }
                        value={this.state.crafting}
                        id="crafting"
                      >
                        crafting <span>{this.state.crafting}</span>
                      </button>
                    </h2>
                    <h2>
                      <button
                        onClick={this.buttonClickedSkill}
                        className={
                          this.state.engineeringChecked
                            ? "button checked"
                            : "button "
                        }
                        value={this.state.engineering}
                        id="engineering"
                      >
                        engineering <span>{this.state.engineering}</span>
                      </button>
                    </h2>
                    <h2>
                      <button
                        onClick={this.buttonClickedSkill}
                        className={
                          this.state.fightingChecked
                            ? "button checked"
                            : "button "
                        }
                        value={this.state.fighting}
                        id="fighting"
                      >
                        fighting <span>{this.state.fighting}</span>
                      </button>
                    </h2>
                    <h2>
                      <button
                        onClick={this.buttonClickedSkill}
                        className={
                          this.state.medicineChecked
                            ? "button checked"
                            : "button "
                        }
                        value={this.state.medicine}
                        id="medicine"
                      >
                        medicine <span>{this.state.medicine}</span>
                      </button>
                    </h2>
                  </div>
                  <div className="spacer"></div>
                  <div className="box-2">
                    <h2>
                      <button
                        onClick={this.buttonClickedSkill}
                        className={
                          this.state.observationChecked
                            ? "button checked"
                            : "button "
                        }
                        value={this.state.observation}
                        id="observation"
                      >
                        observation <span>{this.state.observation}</span>
                      </button>
                    </h2>
                    <h2>
                      <button
                        onClick={this.buttonClickedSkill}
                        className={
                          this.state.persuasionChecked
                            ? "button checked"
                            : "button "
                        }
                        value={this.state.persuasion}
                        id="persuasion"
                      >
                        persuasion <span>{this.state.persuasion}</span>
                      </button>
                    </h2>
                    <h2>
                      <button
                        onClick={this.buttonClickedSkill}
                        className={
                          this.state.resilienceChecked
                            ? "button checked"
                            : "button "
                        }
                        value={this.state.resilience}
                        id="resilience"
                      >
                        resilience <span>{this.state.resilience}</span>
                      </button>
                    </h2>
                    <h2>
                      <button
                        onClick={this.buttonClickedSkill}
                        className={
                          this.state.stealthChecked
                            ? "button checked"
                            : "button "
                        }
                        value={this.state.stealth}
                        id="stealth"
                      >
                        stealth <span>{this.state.stealth}</span>
                      </button>
                    </h2>
                    <h2>
                      <button
                        onClick={this.buttonClickedSkill}
                        className={
                          this.state.survivalChecked
                            ? "button checked"
                            : "button "
                        }
                        value={this.state.survival}
                        id="survival"
                      >
                        survival <span>{this.state.survival}</span>
                      </button>
                    </h2>
                    <h2>
                      <button
                        onClick={this.buttonClickedSkill}
                        className={
                          this.state.tacticsChecked
                            ? "button checked"
                            : "button "
                        }
                        value={this.state.tactics}
                        id="tactics"
                      >
                        tactics <span>{this.state.tactics}</span>
                      </button>
                    </h2>
                  </div>
                </div>
                <div className={"dice-box"}>
                  <label className="form-check-label">Dice </label>
                  <select
                    value={this.state.dice}
                    onChange={this.handledice}
                    className="form-select"
                    aria-label="Wybierz ilosc kosci"
                  >
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value={"4"}>4</option>
                    <option value={"5"}>5</option>
                  </select>
                </div>
                <div className={"box-dice-focus"}>
                  <div className="form-check form-switch focus-box focus">
                    <label className="form-check-label">Focus </label>
                    <input
                      className="form-check-input"
                      type="checkbox"
                      id="flexSwitchCheckDefault"
                      checked={this.state.focusChecked}
                      onChange={this.handleFocusChange}
                    />

                    <button
                      className={"btn btn-dark"}
                      onClick={this.handleSubmitRoll}
                    >
                      Send
                    </button>
                  </div>
                </div>
              </div>
              <div className="CharacterInfo">
                <span id={"info-name"}>Info</span>
                <div className="box-info">
                  <div className="info-box">
                    Focuses{" "}
                    <button
                      className={"btn btn-danger edit-button"}
                      onClick={this.handleEditFocuses}
                    >
                      edit
                    </button>
                    <ul>
                      {this.state.data !== null ? (
                        this.state.data.skills.focus.map((item) => (
                          <li key={item.id}>
                            {item.focus_name} [{item.skill_name}]{" "}
                            {this.state.editFocuses ? (
                              <button
                                className={"x-button"}
                                onClick={() => this.handleDeleteFocus(item.id)}
                              >
                                X
                              </button>
                            ) : (
                              ""
                            )}
                          </li>
                        ))
                      ) : (
                        <span>bad nickname</span>
                      )}
                    </ul>
                    {this.state.editFocuses ? (
                      <div>
                        {" "}
                        <input type={"text"} placeholder={"enter focus..."} />
                        <button>Add</button>{" "}
                      </div>
                    ) : (
                      ""
                    )}
                  </div>
                  <div className="info-box">
                    Truths{" "}
                    <button
                      className={"btn btn-danger edit-button"}
                      onClick={this.handleEditTruths}
                    >
                      edit
                    </button>
                    <ul>
                      {this.state.data !== null ? (
                        this.state.data.truths.map((item) => (
                          <li key={item.id}>
                            {item.description}{" "}
                            {this.state.editTruths ? (
                              <button
                                className={"x-button"}
                                onClick={() => this.handleDeleteTruth(item.id)}
                              >
                                X
                              </button>
                            ) : (
                              ""
                            )}
                          </li>
                        ))
                      ) : (
                        <span>bad nickname</span>
                      )}
                    </ul>
                    <input
                      type="text"
                      placeholder="Enter truth..."
                      value={this.state.input}
                      onChange={this.handleInputChange}
                      onKeyDown={this.handleEnterPress}
                    ></input>
                    <button onClick={this.handleAddTruth}>Add</button>
                  </div>
                </div>
                <div className="box-info">
                  <div className="info-box">
                    Talents
                    <ul>
                      {this.state.data !== null ? (
                        this.state.data.talents.map((item, _) => (
                          <li key={item.id}>{item.name}</li>
                        ))
                      ) : (
                        <span>bad nickname</span>
                      )}
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        ) : (
          <div>Loading....</div>
        )}
      </div>
    );
  }
}
