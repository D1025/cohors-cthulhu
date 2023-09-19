import {Component} from "react";

export default class FormSheet extends Component {
    constructor() {
        super();
        this.maxValAttr = 15;
        this.maxValSkill = 5;
    }
    render() {
        return(
        <div>
        <form action={"/test"} method={"POST"}>
            <div className={"form-group"}>
            <label htmlFor={"nickname"}>Nickname</label>
            <input className={"form-control input"} type={"text"} name={"nickname"} placeholder={"Nickname..."}/>
            </div>
            <div className="spacer-hori"></div>
            <h2>Attributes</h2>
            <div className={"form-group atr"}>
                <div className="atr-box-row">
                        <div className="atr-label-input">
                            <label className={"label"} htmlFor={"agility"}>Agility</label>
                            <input className={"form-control input"} type={"number"} name={"agility"} placeholder={"Agi..."} min={"0"} max={this.maxValAttr}/>
                        </div>
                        <div className="atr-label-input">
                            <label className={"label"} htmlFor={"brawn"}>Brawn</label>
                            <input className={"form-control input"} type={"number"} name={"brawn"} placeholder={"Brawn..."} min={"0"} max={this.maxValAttr}/>
                        </div>
                        <div className="atr-label-input">
                            <label className={"label"} htmlFor={"coord"}>Coordination</label>
                            <input className={"form-control input"} type={"number"} name={"coord"} placeholder={"Coord..."} min={"0"} max={this.maxValAttr}/>
                        </div>
                </div>
                <div className="atr-box-row">
                    <div className="atr-label-input">
                        <label className={"label"} htmlFor={"insight"}>Insight</label>
                        <input className={"form-control input"} type={"number"} name={"insight"} placeholder={"Insight..."} min={"0"} max={this.maxValAttr}/>
                    </div>
                    <div className="atr-label-input">
                        <label className={"label"} htmlFor={"gravitas"}>Gravitas</label>
                        <input className={"form-control input"} type={"number"} name={"gravitas"} placeholder={"Gravitas..."} min={"0"} max={this.maxValAttr}/>
                    </div>
                    <div className="atr-label-input">
                        <label className={"label"} htmlFor={"reason"}>Reason</label>
                        <input className={"form-control input"} type={"number"} name={"reason"} placeholder={"Reason..."} min={"0"} max={this.maxValAttr}/>
                    </div>
                </div>
                <div className="atr-box-row center-verticaly">
                    <div className="atr-label-input">
                        <label htmlFor={"will"} className="label">Will</label>
                        <input type="number" className="form-control input" name={"will"} placeholder={"Will..."} min={"0"} max={this.maxValAttr}/>
                    </div>
                </div>
            </div>
            <div className="spacer-hori"></div>
            <h2>Skills</h2>
            <div className="atr-box-row center-verticaly">
                <div className="atr-label-input">
                    <label className={"label"} htmlFor={"academia"}>Academia</label>
                    <input className={"form-control input"} type={"number"} name={"academia"} placeholder={"Academia..."} min={"0"} max={this.maxValSkill}/>
                </div>
                <div className="atr-label-input">
                    <label className={"label"} htmlFor={"athletics"}>Athletics</label>
                    <input className={"form-control input"} type={"number"} name={"athletics"} placeholder={"Athletics..."} min={"0"} max={this.maxValSkill}/>
                </div>
                <div className="atr-label-input">
                    <label className={"label"} htmlFor={"crafting"}>Crafting</label>
                    <input className={"form-control input"} type={"number"} name={"crafting"} placeholder={"Crafting..."} min={"0"} max={this.maxValSkill}/>
                </div>
            </div>
            <div className="atr-box-row center-verticaly">
                <div className="atr-label-input">
                    <label className={"label"} htmlFor={"fighting"}>Figthing</label>
                    <input className={"form-control input"} type={"number"} name={"fighting"} placeholder={"Fighting..."} min={"0"} max={this.maxValSkill}/>
                </div>
                <div className="atr-label-input">
                    <label className={"label"} htmlFor={"medicine"}>Medicine</label>
                    <input className={"form-control input"} type={"number"} name={"medicine"} placeholder={"Medicine..."} min={"0"} max={this.maxValSkill}/>
                </div>
                <div className="atr-label-input">
                    <label className={"label"} htmlFor={"observation"}>Observation</label>
                    <input className={"form-control input"} type={"number"} name={"observation"} placeholder={"Observation..."} min={"0"} max={this.maxValSkill}/>
                </div>
            </div>
            <div className="atr-box-row center-verticaly">
                <div className="atr-label-input">
                    <label className={"label"} htmlFor={"persuasion"}>Persuasion</label>
                    <input className={"form-control input"} type={"number"} name={"persuasion"} placeholder={"Persuasion..."} min={"0"} max={this.maxValSkill}/>
                </div>
                <div className="atr-label-input">
                    <label className={"label"} htmlFor={"resilience"}>Resilience</label>
                    <input className={"form-control input"} type={"number"} name={"resilience"} placeholder={"Resilience..."} min={"0"} max={this.maxValSkill}/>
                </div>
                <div className="atr-label-input">
                    <label className={"label"} htmlFor={"stealth"}>Stealth</label>
                    <input className={"form-control input"} type={"number"} name={"stealth"} placeholder={"Stealth..."} min={"0"} max={this.maxValSkill}/>
                </div>
            </div>
            <div className="atr-box-row center-verticaly">
                <div className="atr-label-input center-2">
                    <label htmlFor={"survival"} className="label">Survival</label>
                    <input type="number" className="form-control input" name={"survival"} placeholder={"Survival..."} min={"0"} max={this.maxValSkill}/>
                </div>
                <div className="atr-label-input center-2">
                    <label htmlFor={"tactics"} className="label">Tactics</label>
                    <input type="number" className="form-control input" name={"tactics"} placeholder={"Tactics..."} min={"0"} max={this.maxValSkill}/>
                </div>
            </div>
            <div className="spacer-hori"></div>
            <button className={"btn btn-primary"} type={"submit"}>Submit</button>
        </form>
        </div>)
    }
}