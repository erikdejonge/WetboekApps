//
//  BestuursrechtAppDelegate.h
//  Bestuursrecht
//
//  Created by rabshakeh on 10/14/09 - 12:09 PM.
//  Copyright __MyCompanyName__ 2011. All rights reserved.
//

#import <UIKit/UIKit.h>

@class BestuursrechtViewController ;

@interface BestuursrechtAppDelegate : NSObject<UIApplicationDelegate> {
  UIWindow                    *window ;
  BestuursrechtViewController *viewController ;
  UINavigationController      *navigationController ;
}

@property (nonatomic, retain) IBOutlet UIWindow                    *window ;
@property (nonatomic, retain) IBOutlet BestuursrechtViewController *viewController ;

@end
