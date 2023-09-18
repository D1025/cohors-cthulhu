import React from "react";
import "./Sheet.css";

export default class Sheet extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
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
        };
        this.buttonClickedAttr = this.buttonClickedAttr.bind(this);
        this.buttonClickedSkill = this.buttonClickedSkill.bind(this);
        this.handleFocusChange = this.handleFocusChange.bind(this);
    }

    buttonClickedAttr(e) {
        let attribute = e.target.innerHTML.split(" ")[0];

        switch (attribute){
            case 'Agility':
                this.setState((prevState) =>({
                    agiChecked: !prevState.agiChecked,
                    brawnChecked: false,
                    coordChecked: false,
                    insightChecked: false,
                    gravitasChecked: false,
                    reasonChecked: false,
                    willChecked: false,
                }));
                break;
            case 'Brawn':
                this.setState((prevState) =>({
                    agiChecked: false,
                    brawnChecked: !prevState.brawnChecked,
                    coordChecked: false,
                    insightChecked: false,
                    gravitasChecked: false,
                    reasonChecked: false,
                    willChecked: false,
                }));
                break;
            case 'Coordination':
                this.setState((prevState) =>({
                agiChecked: false,
                brawnChecked: false,
                coordChecked: !prevState.coordChecked,
                insightChecked: false,
                gravitasChecked: false,
                reasonChecked: false,
                willChecked: false,
            }));
                break;
            case 'Insight':
                this.setState((prevState) =>({
                    agiChecked: false,
                    brawnChecked: false,
                    coordChecked: false,
                    insightChecked: !prevState.insightChecked,
                    gravitasChecked: false,
                    reasonChecked: false,
                    willChecked: false,
                }));
                break;
            case 'Gravitas':
                this.setState((prevState) =>({
                    agiChecked: false,
                    brawnChecked: false,
                    coordChecked: false,
                    insightChecked: false,
                    gravitasChecked: !prevState.gravitasChecked,
                    reasonChecked: false,
                    willChecked: false,
                }));
                break;
            case 'Reason':
                this.setState((prevState) =>({
                    agiChecked: false,
                    brawnChecked: false,
                    coordChecked: false,
                    insightChecked: false,
                    gravitasChecked: false,
                    reasonChecked: !prevState.reasonChecked,
                    willChecked: false,
                }));
                break;
            case 'Will':
                this.setState((prevState) =>({
                    agiChecked: false,
                    brawnChecked: false,
                    coordChecked: false,
                    insightChecked: false,
                    gravitasChecked: false,
                    reasonChecked: false,
                    willChecked: !prevState.willChecked,
                }));
                break;
        }



    }
    buttonClickedSkill(e){
        let skillName = e.target.innerHTML.split(" ")[0];
        switch(skillName){
            case 'academia':
                this.setState((prevState)=>({
                    academiaChecked: !prevState.academiaChecked,
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
                }))
                break;
            case 'athletics':
                this.setState((prevState)=>({
                    academiaChecked: false,
                    athleticsChecked: !prevState.athleticsChecked,
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
                }))
                break;
            case 'crafting':
                this.setState((prevState)=>({
                    academiaChecked: false,
                    athleticsChecked: false,
                    craftingChecked: !prevState.craftingChecked,
                    engineeringChecked: false,
                    fightingChecked: false,
                    medicineChecked: false,
                    observationChecked: false,
                    persuasionChecked: false,
                    resilienceChecked: false,
                    stealthChecked: false,
                    survivalChecked: false,
                    tacticsChecked: false,
                }))
                break;
            case "engineering":
                this.setState((prevState)=>({
                    academiaChecked: false,
                    athleticsChecked: false,
                    craftingChecked: false,
                    engineeringChecked: !prevState.engineeringChecked,
                    fightingChecked: false,
                    medicineChecked: false,
                    observationChecked: false,
                    persuasionChecked: false,
                    resilienceChecked: false,
                    stealthChecked: false,
                    survivalChecked: false,
                    tacticsChecked: false,
                }))
                break;
            case "fighting":
                this.setState((prevState)=>({
                    academiaChecked: false,
                    athleticsChecked: false,
                    craftingChecked: false,
                    engineeringChecked: false,
                    fightingChecked: !prevState.fightingChecked,
                    medicineChecked: false,
                    observationChecked: false,
                    persuasionChecked: false,
                    resilienceChecked: false,
                    stealthChecked: false,
                    survivalChecked: false,
                    tacticsChecked: false,
                }))
                break;
            case "medicine":
                this.setState((prevState)=>({
                    academiaChecked: false,
                    athleticsChecked: false,
                    craftingChecked: false,
                    engineeringChecked: false,
                    fightingChecked: false,
                    medicineChecked: !prevState.medicineChecked,
                    observationChecked: false,
                    persuasionChecked: false,
                    resilienceChecked: false,
                    stealthChecked: false,
                    survivalChecked: false,
                    tacticsChecked: false,
                }))
                break;
            case "observation":
                this.setState((prevState)=>({
                    academiaChecked: false,
                    athleticsChecked: false,
                    craftingChecked: false,
                    engineeringChecked: false,
                    fightingChecked: false,
                    medicineChecked: false,
                    observationChecked: !prevState.observationChecked,
                    persuasionChecked: false,
                    resilienceChecked: false,
                    stealthChecked: false,
                    survivalChecked: false,
                    tacticsChecked: false,
                }))
                break;
            case "persuasion":
                this.setState((prevState)=>({
                    academiaChecked: false,
                    athleticsChecked: false,
                    craftingChecked: false,
                    engineeringChecked: false,
                    fightingChecked: false,
                    medicineChecked: false,
                    observationChecked: false,
                    persuasionChecked: !prevState.persuasionChecked,
                    resilienceChecked: false,
                    stealthChecked: false,
                    survivalChecked: false,
                    tacticsChecked: false,
                }))
                break;
            case "resilience":
                this.setState((prevState)=>({
                    academiaChecked: false,
                    athleticsChecked: false,
                    craftingChecked: false,
                    engineeringChecked: false,
                    fightingChecked: false,
                    medicineChecked: false,
                    observationChecked: false,
                    persuasionChecked: false,
                    resilienceChecked: !prevState.resilienceChecked,
                    stealthChecked: false,
                    survivalChecked: false,
                    tacticsChecked: false,
                }))
                break;
            case "stealth":
                this.setState((prevState)=>({
                    academiaChecked: false,
                    athleticsChecked: false,
                    craftingChecked: false,
                    engineeringChecked: false,
                    fightingChecked: false,
                    medicineChecked: false,
                    observationChecked: false,
                    persuasionChecked: false,
                    resilienceChecked: false,
                    stealthChecked: !prevState.resilienceChecked,
                    survivalChecked: false,
                    tacticsChecked: false,
                }))
                break;
            case "survival":
                this.setState((prevState)=>({
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
                    survivalChecked: !prevState.survivalChecked,
                    tacticsChecked: false,
                }))
                break;
            case "tactics":
                this.setState((prevState)=>({
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
                    tacticsChecked: !prevState.tacticsChecked,
                }))
                break;
        }

    }
    handleFocusChange = () => {
        this.setState((prevState)=>({
            focusChecked: !prevState.focusChecked,
        }))
    }
    handleSubmitRoll = ()=>{
        let skill = "";
        let skillVal = 0;
        let attribute = "";
        let attrVal = 0;
        if (this.state.agiChecked){
            attribute = "agility";
            attrVal = this.state.agi;
        }
        else if(this.state.brawnChecked){
            attribute = "brawn";
            attrVal = this.state.brawn;
        }
        else if(this.state.coordChecked){
            attribute = "coordination";
            attrVal = this.state.coord;
        }
        else if(this.state.insightChecked){
            attribute = "insight";
            attrVal = this.state.insight;
        }
        else if(this.state.gravitasChecked){
            attribute = "gravitas";
            attrVal = this.state.gravitas;
        }
        else if(this.state.reasonChecked){
            attribute = "reason";
            attrVal = this.state.reason;
        }
        else if(this.state.willChecked){
            attribute = "will";
            attrVal = this.state.will;
        }
        else{
            alert("No skill checked");
            return;
        }
        if(this.state.academiaChecked){
            skill = "academia";
            skillVal = this.state.academia;
        }
        else if(this.state.athleticsChecked){
            skill = "athletics";
            skillVal = this.state.athletics;
        }
        else if(this.state.craftingChecked){
            skill = "crafting";
            skillVal = this.state.crafting;
        }
        else if(this.state.engineeringChecked){
            skill = "engineering";
            skillVal = this.state.engineering;
        }
        else if(this.state.fightingChecked){
            skill = "fighting";
            skillVal = this.state.fighting;
        }
        else if(this.state.medicineChecked){
            skill = "medicine";
            skillVal = this.state.medicine;
        }
        else if(this.state.observationChecked){
            skill = "observation";
            skillVal = this.state.observation;
        }
        else if(this.state.persuasionChecked){
            skill = "persuasion";
            skillVal = this.state.persuasion;
        }
        else if(this.state.resilienceChecked){
            skill = "resilience";
            skillVal = this.state.resilience;
        }
        else if(this.state.stealthChecked){
            skill = "stealth";
            skillVal = this.state.stealth;
        }
        else if(this.state.survivalChecked){
            skill = "survival";
            skillVal = this.state.survival;
        }
        else if(this.state.tacticsChecked){
            skill = "tactics";
            skillVal = this.state.tactics;
        }
        else{
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
        }
        this.props.ws.send(JSON.stringify(message))
    }

    handledice = (e)=>{
        this.setState((prevState) => ({
            dice: parseInt(e.target.value),
        }))
    }
    componentDidMount() {
        fetch(`http://104.248.37.81:8087/character?name=${this.props.nickname}`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then((data) => {
            this.setState({
                    agi: data.attributes.agility,
                    brawn: data.attributes.brawn,
                    coord: data.attributes.coordination,
                    insight: data.attributes.insight,
                    gravitas: data.attributes.gravitas,
                    reason: data.attributes.reason,
                    will: data.attributes.will,
                    academia: data.skills.academia,
                    athletics: data.skills.athletics,
                    crafting: data.skills.crafting,
                    engineering: data.skills.engineering,
                    fighting: data.skills.fighting,
                    medicine: data.skills.medicine,
                    observation: data.skills.observation,
                    persuasion: data.skills.persuasion,
                    resilience: data.skills.resilience,
                    stealth: data.skills.stealth,
                    survival: data.skills.survival,
                    tactics: data.skills.tactics,
                data: data,
                isLoading: false, // Update isLoading to false
                error: null,
            }
            );

            })
            .catch((error) => {
                console.error('API Error:', error); // Log any error
                this.setState({
                    error: error,
                    isLoading: false,
                });
            });

    }

    render() {

        return <div>
            { !this.state.isLoading ? (<div className={"entire"}>
                <div className="CharacterSheet">
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
                                        className={ this.state.agiChecked ? 'button checked' : 'button'}
                                    >
                                        Agility <span>{this.state.agi}</span>
                                    </button>
                                </h2>

                                <h2>
                                    <button
                                        onClick={this.buttonClickedAttr}
                                        id="brawn-value"
                                        className={ this.state.brawnChecked ? "button checked" : 'button '}
                                    >
                                        Brawn <span>{this.state.brawn}</span>
                                    </button>
                                </h2>

                                <h2>
                                    <button
                                        onClick={this.buttonClickedAttr}
                                        id="coord-value"
                                        className={this.state.coordChecked ? "button checked" : 'button '}

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
                                        className={this.state.insightChecked ? "button checked" : 'button '}

                                    >
                                        Insight <span>{this.state.insight}</span>
                                    </button>
                                </h2>

                                <h2>
                                    <button
                                        onClick={this.buttonClickedAttr}
                                        id="gravi-value"
                                        className={this.state.gravitasChecked ? "button checked" : 'button '}

                                    >
                                        Gravitas <span>{this.state.gravitas}</span>
                                    </button>
                                </h2>

                                <h2>
                                    <button
                                        onClick={this.buttonClickedAttr}
                                        id="reason-value"
                                        className={this.state.reasonChecked ? "button checked" : 'button '}

                                    >
                                        Reason <span>{this.state.reason}</span>
                                    </button>
                                </h2>

                                <h2>
                                    <button
                                        onClick={this.buttonClickedAttr}
                                        id="will-value"
                                        className={this.state.willChecked ? "button checked" : 'button '}
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
                                        className={this.state.academiaChecked ? "button checked" : 'button '}
                                        value={this.state.academia}
                                        id="academia">academia <span>{this.state.academia}</span></button>
                                </h2>

                                <h2>
                                    <button
                                        onClick={this.buttonClickedSkill}
                                        className={this.state.athleticsChecked ? "button checked" : 'button '}
                                        value={this.state.athletics}
                                        id="athletics">athletics <span>{this.state.athletics}</span></button>
                                </h2>
                                <h2>
                                    <button
                                        onClick={this.buttonClickedSkill}
                                        className={this.state.craftingChecked ? "button checked" : 'button '}
                                        value={this.state.crafting}
                                        id="crafting">crafting <span>{this.state.crafting}</span></button>
                                </h2>
                                <h2>
                                    <button
                                        onClick={this.buttonClickedSkill}
                                        className={this.state.engineeringChecked ? "button checked" : 'button '}
                                        value={this.state.engineering}
                                        id="engineering">engineering <span>{this.state.engineering}</span></button>
                                </h2>
                                <h2>
                                    <button
                                        onClick={this.buttonClickedSkill}
                                        className={this.state.fightingChecked ? "button checked" : 'button '}
                                        value={this.state.fighting}
                                        id="fighting">fighting <span>{this.state.fighting}</span></button>
                                </h2>
                                <h2>
                                    <button
                                        onClick={this.buttonClickedSkill}
                                        className={this.state.medicineChecked ? "button checked" : 'button '}
                                        value={this.state.medicine}
                                        id="medicine">medicine <span>{this.state.medicine}</span></button>
                                </h2>
                            </div>
                            <div className="spacer"></div>
                            <div className="box-2">
                                <h2>
                                    <button onClick={this.buttonClickedSkill}
                                            className={this.state.observationChecked ? "button checked" : 'button '}
                                            value={this.state.observation}
                                            id="observation">observation <span>{this.state.observation}</span></button>
                                </h2>
                                <h2>
                                    <button onClick={this.buttonClickedSkill}
                                            className={this.state.persuasionChecked ? "button checked" : 'button '}
                                            value={this.state.persuasion}
                                            id="persuasion">persuasion <span>{this.state.persuasion}</span></button>
                                </h2>
                                <h2>
                                    <button onClick={this.buttonClickedSkill}
                                            className={this.state.resilienceChecked ? "button checked" : 'button '}
                                            value={this.state.resilience}
                                            id="resilience">resilience <span>{this.state.resilience}</span></button>
                                </h2>
                                <h2>
                                    <button onClick={this.buttonClickedSkill}
                                            className={this.state.stealthChecked ? "button checked" : 'button '}
                                            value={this.state.stealth}
                                            id="stealth">stealth <span>{this.state.stealth}</span></button>
                                </h2>
                                <h2>
                                    <button onClick={this.buttonClickedSkill}
                                            className={this.state.survivalChecked ? "button checked" : 'button '}
                                            value={this.state.survival}
                                            id="survival">survival <span>{this.state.survival}</span></button>
                                </h2>
                                <h2>
                                    <button onClick={this.buttonClickedSkill}
                                            className={this.state.tacticsChecked ? "button checked" : 'button '}
                                            value={this.state.tactics}
                                            id="tactics">tactics <span>{this.state.tactics}</span></button>
                                </h2>

                            </div>
                        </div>
                        <div className={"dice-box"}>
                            <label className="form-check-label" >Dice </label>
                            <select value={this.state.dice} onChange={this.handledice} className="form-select" aria-label="Wybierz ilosc kosci">
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                                <option value={"4"}>4</option>
                                <option value={"5"}>5</option>
                            </select>
                        </div>
                        <div className={"box-dice-focus"}>
                            <div className="form-check form-switch focus-box focus">
                                <label className="form-check-label" >Focus  </label>
                                <input className="form-check-input" type="checkbox" id="flexSwitchCheckDefault" checked={this.state.focusChecked} onChange={this.handleFocusChange} />

                                <button className={"btn btn-dark"} onClick={this.handleSubmitRoll}>Send</button>
                            </div>

                        </div>
                    </div>
                    <div className="CharacterInfo">
                        <span id={"info-name"}>Info</span>
                        <div className="box-info">
                            <div className="info-box">
                                Focuses
                                <ul>
                                    {this.state.data.skills.focus.map((item, index) => (
                                        <li key={index}>{item.focus_name} [{item.skill_name}]</li>
                                    ))}
                                </ul>
                            </div>
                            <div className="info-box">
                                Languages
                                <ul>
                                    {this.state.data.truths.map((item, index)=>(
                                        <li key={index}>{item.description}</li>
                                    ))}
                                </ul>
                            </div>
                        </div>
                        <div className="box-info">
                        <div className="info-box">
                            Talents
                            <ul>
                            {this.state.data.talents.map((item, index)=>(
                                <li key={index}>{item.name}</li>
                            ))}
                            </ul>
                        </div>
                    </div>
                        </div>
                </div>
            </div>) : (
                <div>Loading....</div>
            )}
        </div>
    }
}
