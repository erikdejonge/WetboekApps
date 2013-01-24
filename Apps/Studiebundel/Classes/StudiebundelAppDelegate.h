//
//  StudiebundelAppDelegate.h
//  Studiebundel
//
//  Created by rabshakeh on 8/25/09 - 12:52 PM.
//  Copyright __MyCompanyName__ 2011. All rights reserved.
//

#import <UIKit/UIKit.h>

@class WetboekRootViewController;

@interface StudiebundelAppDelegate : NSObject<UIApplicationDelegate> {
  UIWindow                  *window;
  WetboekRootViewController *viewController;
  UINavigationController    *navigationController;
}

@property (nonatomic, retain) IBOutlet UIWindow                  *window;
@property (nonatomic, retain) IBOutlet WetboekRootViewController *viewController;

@end

