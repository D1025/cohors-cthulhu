import {Component} from "react";
import './Creation.css'
import FormSheet from './FormSheet'
export default class Creation extends Component {
    constructor() {
        super();
    }
    render() {
        return(
            <div className={"container center-content"}>
                <div className={"box-creation"}>
                    <FormSheet />
                </div>
            </div>
        )
    }
}