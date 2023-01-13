
import './AnimatedText.scss'
const AnimatedText = ({text}) => {
    
    return ( 
        <div className = "animated-text-container">
            {[...text].map(words => 
            <div className = "animated-text-item">
                {words}
            </div>
            )} 
        </div>
     );
}
 
export default AnimatedText;