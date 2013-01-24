//
//  SociaalrechtAppDelegate.h
//  Sociaalrecht
//
//  Created by rabshakeh on 9/17/09 - 12:29 PM.
//  Copyright __MyCompanyName__ 2011. All rights reserved.
//

#import <UIKit/UIKit.h>

@class SociaalrechtViewController;

@interface SociaalrechtAppDelegate : NSObject<UIApplicationDelegate> {
  UIWindow                   *window;
  SociaalrechtViewController *viewController;
  UINavigationController     *navigationController;
}

@property (nonatomic, retain) IBOutlet UIWindow                   *window;
@property (nonatomic, retain) IBOutlet SociaalrechtViewController *viewController;

@end
