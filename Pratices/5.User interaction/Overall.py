'''
1. interaction action ( mouse action ) - mouse what kindly use that we do in selenium
                                         we create object for ActionChains class
                                         object was access to moues work
                                         double click,drag,move,right click
                                         above all do in ActionChains class


2. handling child window or tab -      driver access main(parent) tab to another(child) tab,
                                        selenium can't access to child tab
                                        we switch to child tab
                                        name we need.so, we use window.handles, it used for get tab name, and we pass parameter
                                        driver.switch_to_window(tab name)

                                        if we want back to parent tab we need again change child to parent




3. frame handling -                     frame is embedded HTML, it placed in top oof the HTML, it looked link an HTML, but not.
                                        selenium not knowledge for access frame( can't access directly )
                                        we need switch to frame ( like an alert handle )
                                        driver.switch_to.frame(frame reference)  - frame reference ID or NAME values
                                        once do in frame again we  change to normal
                                        driver.switch_to.default_content()  - not give any parameter

'''