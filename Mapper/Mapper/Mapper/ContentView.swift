//
//  ContentView.swift
//  Mapper
//
//  Created by Vihan Karuthodiyil on 12/18/22.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        
        VStack {
            class ViewController: UIViewController {

                @IBOutlet weak
                var button: UIButton!
                
                override func viewDidLoad() {
                    self.viewDidLoad()
                    
                    // Configure the button
                    button.setTitle("Tap me!", for: .normal)
                    button.setTitleColor(.blue, for: .normal)
                    button.addTarget(self, action: #selector(buttonTapped), for: .touchUpInside)
                }
                
                @objc func buttonTapped() {
                    // Show an alert when the button is tapped
                    let alert = UIAlertController(title: "Button Tapped", message: "You tapped the button!", preferredStyle: .alert)
                    alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
                    present(alert, animated: true, completion: nil)
                }
            }

           
        }
        .padding()
    }
    
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
