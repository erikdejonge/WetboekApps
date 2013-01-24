//
//  StrafrechtAppDelegate.h
//  Strafrecht
//
//  Created by rabshakeh on 8/18/09 - 3:54 PM.
//  Copyright __MyCompanyName__ 2011. All rights reserved.
//

#import <UIKit/UIKit.h>

@class WetboekRootViewController;

@interface StrafrechtAppDelegate : NSObject<UIApplicationDelegate> {
  UIWindow                  *window;
  WetboekRootViewController *viewController;
  UINavigationController    *navigationController;
}

@property (nonatomic, retain) IBOutlet UIWindow                  *window;
@property (nonatomic, retain) IBOutlet WetboekRootViewController *viewController;

@end

