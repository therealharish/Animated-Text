
import './home.css'
import AnimatedText from '../AnimatedText/AnimatedText';

const Home = () => {
    return ( 
        <div>
        <div className = "main">
            <h2>We</h2>
            <h2>Are</h2>
            <h2>An Activist Community</h2>
            <p>Bringing justice to you!</p>
        </div>
        <div className = "circle"></div>
        <div>
            <AnimatedText text = "wellwecare" />
        </div>
        </div>
     );
}
 
export default Home;