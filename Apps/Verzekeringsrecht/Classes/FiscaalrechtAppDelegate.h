//
//  FiscaalrechtAppDelegate.h
//  Fiscaalrecht
//
//  Created by rabshakeh on 8/19/09 - 2:23 PM.
//  Copyright __MyCompanyName__ 2010. All rights reserved.
//

#import <UIKit/UIKit.h>

@class WetboekRootViewController ;

@interface FiscaalrechtAppDelegate : NSObject<UIApplicationDelegate> {
  UIWindow                  *window ;
  WetboekRootViewController *viewController ;
  UINavigationController    *navigationController ;
}

@property (nonatomic, retain) IBOutlet UIWindow                  *window ;
@property (nonatomic, retain) IBOutlet WetboekRootViewController *viewController ;

@end

