//
//  PolitierechtAppDelegate.h
//  Politierecht
//
//  Created by rabshakeh on 9/28/09 - 3:10 PM.
//  Copyright __MyCompanyName__ 2011. All rights reserved.
//

#import <UIKit/UIKit.h>

@class PolitierechtViewController ;

@interface PolitierechtAppDelegate : NSObject<UIApplicationDelegate> {
  UIWindow                   *window ;
  PolitierechtViewController *viewController ;
  UINavigationController     *navigationController ;
}

@property (nonatomic, retain) IBOutlet UIWindow                   *window ;
@property (nonatomic, retain) IBOutlet PolitierechtViewController *viewController ;


@end

