//
//  Recht_LiteAppDelegate.h
//  Recht Lite
//
//  Created by rabshakeh on 10/14/09 - 12:19 PM.
//  Copyright __MyCompanyName__ 2011. All rights reserved.
//

#import <UIKit/UIKit.h>

@class Recht_LiteViewController ;

@interface Recht_LiteAppDelegate : NSObject<UIApplicationDelegate> {
  UIWindow                 *window ;
  Recht_LiteViewController *viewController ;
  UINavigationController   *navigationController ;
}

@property (nonatomic, retain) IBOutlet UIWindow                 *window ;
@property (nonatomic, retain) IBOutlet Recht_LiteViewController *viewController ;

@end
